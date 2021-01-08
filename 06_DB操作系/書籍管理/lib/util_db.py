import datetime, sqlite3, os

class Book:
    def __init__(self, db_file, mode, data_id, isbn='', name='', author='', translator=''
                , publisher='', selling_agency='', original_price=0, bid_price=0, selling_price=0
                , owned_flg='', remarks='', tag=''):
        self.db_init(db_file)
        row = self.select_by_key(data_id)
        # 新規登録
        if row is None:
            self.data_id = data_id               # data_id
            self.isbn = isbn                     # ISBN
            self.name = name                     # 名称
            self.author = author                 # 著者
            self.translator = translator         # 翻訳者
            self.publisher = publisher           # 発行元
            self.selling_agency = selling_agency # 発売元
            self.original_price = original_price # 定価
            self.bid_price = bid_price           # 買値
            self.selling_price = selling_price   # 売値
            self.owned_flg = owned_flg           # 所有フラグ(0:売却済み/1:持ってる)
            self.remarks = remarks               # 備考
            self.tag = tag                       # タグ
        else:
            if mode == 'update':
                self.data_id = row[0]
                self.isbn = isbn if isbn != '' else row[1]
                self.name = name if name != '' else row[2]
                self.author = author if author != '' else row[3]
                self.translator = translator if translator != '' else row[4]
                self.publisher = publisher if publisher != '' else row[5]
                self.selling_agency = selling_agency if selling_agency != '' else row[6]
                self.original_price = original_price if original_price != 0 else row[7]
                self.bid_price = bid_price if bid_price != 0 else row[8]
                self.selling_price = selling_price if selling_price != 0 else row[9]
                self.owned_flg = owned_flg if owned_flg != '' else row[10]
                self.remarks = remarks if remarks != '' else row[11]
                self.tag = tag if tag != '' else row[12]
            else:
                self.data_id = row[0]
                self.isbn = row[1]
                self.name = row[2]
                self.author = row[3]
                self.translator = row[4]
                self.publisher = row[5]
                self.selling_agency = row[6]
                self.original_price = row[7]
                self.bid_price = row[8]
                self.selling_price = row[9]
                self.owned_flg = row[10]
                self.remarks = row[11]
                self.tag = row[12]
        # print(self.data_id)
        # print(self.isbn)
        # print(self.name)
        # print(self.author)
        # print(self.translator)
        # print(self.publisher)
        # print(self.selling_agency)
        # print(self.original_price)
        # print(self.bid_price)
        # print(self.selling_price)
        # print(self.owned_flg)
        # print(self.remarks)
        # print(self.tag)

    @classmethod
    def db_init(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.conn.execute('''
                CREATE TABLE IF NOT EXISTS books(
                      data_id INTEGER PRIMARY KEY AUTOINCREMENT
                    , isbn TEXT
                    , name TEXT
                    , author TEXT
                    , translator TEXT
                    , publisher TEXT
                    , selling_agency TEXT
                    , original_price INTEGER
                    , bid_price INTEGER
                    , selling_price INTEGER
                    , owned_flg INTEGER
                    , remarks TEXT
                    , tag TEXT
                    , regist_datetime TEXT
                    , update_datetime TEXT
                    , delete_datetime TEXT
                )
            ''')
        self.conn.commit()

    def db_close(self):
        self.conn.close()

    def save(self):
        """
        データベースに保存
        """
        ins = ("""
                INSERT INTO 
                    books(
                          isbn
                        , name
                        , author
                        , translator
                        , publisher
                        , selling_agency
                        , original_price
                        , bid_price
                        , selling_price
                        , owned_flg
                        , remarks
                        , tag
                        , regist_datetime
                    )
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))
            """)
        self.conn.execute(ins, (self.isbn, self.name, self.author, self.translator
                                , self.publisher, self.selling_agency
                                , self.original_price, self.bid_price
                                , self.selling_price, self.owned_flg, self.remarks, self.tag))
        self.conn.commit()


    def select_max_seq(self, table_name):
        """
        最大シーケンス取得
        """
        curs = self.conn.cursor()
        select = 'SELECT seq FROM sqlite_sequence WHERE name = ?'
        curs.execute(select, (table_name,))
        row = curs.fetchone()
        curs.close()
        return row[0]

    def select_by_key(self, data_id):
        """
        キーで１件取得
        """
        curs = self.conn.cursor()
        select = '''
                    SELECT
                          data_id
                        , isbn
                        , name
                        , author
                        , translator
                        , publisher
                        , selling_agency
                        , original_price
                        , bid_price
                        , selling_price
                        , owned_flg
                        , remarks
                        , tag
                        , regist_datetime
                        , update_datetime
                        , delete_datetime
                    FROM
                        books
                    WHERE
                        data_id = ?
                '''
        curs.execute(select, (data_id,))
        row = curs.fetchone()
        curs.close()
        return row

    def update_by_key(self):
        """
        キーで更新
        """
        upd = '''
                    UPDATE
                        books 
                    SET
                          isbn = ?
                        , name = ?
                        , author = ?
                        , translator = ?
                        , publisher = ?
                        , selling_agency = ?
                        , original_price = ?
                        , bid_price = ?
                        , selling_price = ?
                        , owned_flg = ?
                        , remarks = ?
                        , tag = ?
                        , update_datetime = datetime('now', 'localtime')
                    WHERE
                        data_id = ?
                '''
        print(self.bid_price)
        print(self.selling_price)
        self.conn.execute(upd, (self.isbn, self.name, self.author, self.translator
                                , self.publisher, self.selling_agency
                                , self.original_price, self.bid_price, self.selling_price
                                , self.owned_flg, self.remarks, self.tag, self.data_id))
        self.conn.commit()

    def delete_by_key(self, data_id):
        """
        キーで削除
        """
        delete = ('DELETE FROM books WHERE data_id = ?')
        self.conn.execute(delete, (data_id, ))
        self.conn.commit()

    @classmethod
    def select_all(self, db_file):
        """
        データベースから全件取得
        """
        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        select = '''
                    SELECT
                          data_id
                        , isbn
                        , name
                        , author
                        , translator
                        , publisher
                        , selling_agency
                        , original_price
                        , bid_price
                        , selling_price
                        , owned_flg
                        , remarks
                        , tag
                        , regist_datetime
                        , update_datetime
                        , delete_datetime
                    FROM
                        books
                    ORDER BY
                        regist_datetime
                '''
        curs.execute(select)
        rows = curs.fetchall()
        curs.close()
        conn.close()
        list = []
        for row in rows:
            book = Book(db_file, 'view', row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                            , row[7], row[8], row[9], row[10], row[11], row[12])
            list.append(book)
        return list


    @classmethod
    def select_by_keyword(self, db_file, keyword):
        """
        データベースから全件取得
        """
        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        select = '''
                    SELECT
                          data_id
                        , isbn
                        , name
                        , author
                        , translator
                        , publisher
                        , selling_agency
                        , original_price
                        , bid_price
                        , selling_price
                        , owned_flg
                        , remarks
                        , tag
                        , regist_datetime
                        , update_datetime
                        , delete_datetime
                    FROM
                        books
                    WHERE
                        name like ?
                     OR author like ?
                     OR translator like ?
                     OR publisher like ?
                     OR selling_agency like ?
                     OR remarks like ?
                     OR tag like ?
                    ORDER BY
                        regist_datetime
                '''
        curs.execute(select, ('%'+keyword+'%','%'+keyword+'%','%'+keyword+'%','%'+keyword+'%','%'+keyword+'%','%'+keyword+'%','%'+keyword+'%',))
        rows = curs.fetchall()
        curs.close()
        conn.close()
        list = []
        for row in rows:
            book = Book(db_file, 'view', row[0], row[1], row[2], row[3], row[4], row[5], row[6]
                            , row[7], row[8], row[9], row[10], row[11], row[12])
            list.append(book)
        return list
