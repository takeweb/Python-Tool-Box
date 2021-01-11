import datetime, sqlite3

class Health:
    data_id = 0
    regist_datetime = ''
    height = 0.0
    weight = 0.0
    bmi = 0.0
    def __init__(self, data_id, regist_datetime, height, weight, bmi):
        self.data_id = data_id
        self.regist_datetime = regist_datetime
        self.height = height
        self.weight = weight
        self.bmi = bmi

class DbUtil:
    def __init__(self, db_file):
        self.db_init(db_file)

    @classmethod
    def db_init(self, db_file):
        self.db_file = db_file
        conn = sqlite3.connect(self.db_file)
        conn.execute('''CREATE TABLE IF NOT EXISTS health(
                            data_id INTEGER PRIMARY KEY AUTOINCREMENT
                            , regist_datetime TEXT
                            , height FLOAT
                            , weight FLOAT
                            , bmi FLOAT)''')
        conn.close()

    def select_for_graph(self, from_date, to_date):
        """
        指定期間のグラフ用データ取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                        strftime('%d', date(regist_datetime))
                        , weight 
                    FROM health 
                    WHERE regist_datetime BETWEEN ? AND ?
                    ORDER BY regist_datetime'''
        to_date = self.get_to_date_for_search(to_date)
        curs.execute(select, (from_date, to_date))
        rows = curs.fetchall()
        curs.close()
        conn.close()
        return rows

    def save(self, health):
        """
        データベースに保存
        """
        conn = sqlite3.connect(self.db_file)
        ins = ('INSERT INTO health(regist_datetime, height, weight, bmi) VALUES(?, ?, ?, ?)')
        conn.execute(ins, (health.regist_datetime, health.height, health.weight, health.bmi))
        conn.commit()
        conn.close()

    def select_all(self):
        """
        データベースから全件取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT 
                          data_id
                        , regist_datetime
                        , height
                        , weight
                        , bmi
                    FROM
                        health
                    ORDER BY
                        regist_datetime DESC'''
        curs.execute(select)
        rows = curs.fetchall()
        curs.close()
        list = []
        for row in rows:
            health = Health(row[0], row[1], row[2], row[3], row[4])
            list.append(health)
        conn.close()
        return list

    def select_max_seq(self, table_name):
        """
        最大シーケンス取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = 'SELECT seq FROM sqlite_sequence WHERE name = ?'
        curs.execute(select, (table_name,))
        row = curs.fetchone()
        curs.close()
        conn.close()
        return row[0]

    def select_max_id(self):
        """
        最新の登録日時のデータIDを取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                          data_id
                    FROM
                        health
                    WHERE
                        regist_datetime = (SELECT MAX(regist_datetime) FROM health)
                '''
        curs.execute(select)
        row = curs.fetchone()
        curs.close()
        conn.close()
        return row[0]

    def select_by_key(self, data_id):
        """
        キーで１件取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                    data_id
                        , regist_datetime
                        , height
                        , weight
                        , bmi
                    FROM
                        health
                    WHERE
                        data_id = ?'''
        curs.execute(select, (data_id,))
        row = curs.fetchone()
        curs.close()
        health = Health(row[0], row[1], row[2], row[3], row[4])
        conn.close()
        return health

    def select_max_weight(self):
        """
        最大体重だった日のデータを取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                          data_id
                        , regist_datetime
                        , height
                        , weight
                        , bmi
                    FROM
                        health
                    WHERE
                        weight = (SELECT MAX(weight) FROM health)
                '''
        curs.execute(select)
        row = curs.fetchone()
        curs.close()
        health = Health(row[0], row[1], row[2], row[3], row[4])
        conn.close()
        return health

    def select_min_weight(self):
        """
        最小体重だった日のデータを取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                          data_id
                        , regist_datetime
                        , height
                        , weight
                        , bmi
                    FROM
                        health
                    WHERE
                        weight = (SELECT MIN(weight) FROM health)
                '''
        curs.execute(select)
        row = curs.fetchone()
        curs.close()
        health = Health(row[0], row[1], row[2], row[3], row[4])
        conn.close()
        return health

    def get_disp_min_max_avg(self, from_date, to_date):
        """
        指定期間の最小体重、最大体重、平均体重をまとめて取得、表示文字列で返却
        """
        avg_weight = self.select_ave_weight_term(str(from_date), str(to_date))
        min_weight = self.select_min_weight_term(str(from_date), str(to_date))
        max_weight = self.select_max_weight_term(str(from_date), str(to_date))
        return 'MIN:' + str(min_weight) + 'kg / AVG:' + str(avg_weight) + 'kg'' / MAX:' + str(max_weight) + 'kg'

    def select_min_weight_term(self, from_date, to_date):
        """
        指定期間の最小体重を取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                        MIN(weight)
                    FROM
                        health
                    WHERE
                        regist_datetime BETWEEN ? AND ?
                '''
        curs.execute(select, (from_date, to_date))
        row = curs.fetchone()
        curs.close()
        conn.close()
        return round(row[0], 1)

    def select_max_weight_term(self, from_date, to_date):
        """
        指定期間の最大体重を取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                        MAX(weight)
                    FROM
                        health
                    WHERE
                        regist_datetime BETWEEN ? AND ?
                '''
        curs.execute(select, (from_date, to_date))
        row = curs.fetchone()
        curs.close()
        conn.close()
        return round(row[0], 1)

    def select_ave_weight_term(self, from_date, to_date):
        """
        指定期間の平均体重を取得
        """
        conn = sqlite3.connect(self.db_file)
        curs = conn.cursor()
        select = '''SELECT
                        AVG(weight) 
                    FROM
                        health
                    WHERE
                        regist_datetime BETWEEN ? AND ?
                '''
        to_date = self.get_to_date_for_search(to_date)
        curs.execute(select, (from_date, to_date))
        row = curs.fetchone()
        curs.close()
        conn.close()
        return round(row[0], 1)

    def update(self, health):
        """
        キーで更新
        """
        conn = sqlite3.connect(self.db_file)
        upd = ('''UPDATE health 
                    SET
                          regist_datetime = ?
                        , height = ? 
                        , weight = ? 
                        , bmi = ?
                    WHERE data_id = ?''')
        conn.execute(upd, (health.regist_datetime, health.height, health.weight, health.bmi, health.data_id))
        conn.commit()
        conn.close()

    def delete_by_key(self, data_id):
        """
        キーで削除
        """
        conn = sqlite3.connect(self.db_file)
        delete = ('DELETE FROM health WHERE data_id = ?')
        conn.execute(delete, (data_id, ))
        conn.commit()
        conn.close()

    def get_to_date_for_search(self, to_date):
        """
        日付で検索する場合、時刻部分がが「00:00:00」で検索されることになるので、
        TO日時は23:59:59を加算してSQLへバインドする
        """
        dt_to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
        dt_to_date = dt_to_date + datetime.timedelta(hours=23, minutes=59)
        to_date = dt_to_date.strftime('%Y-%m-%d %H:%M')

        return to_date

    # def __exit__(self, exc_type, exc_value, traceback):
    #     self.conn.close()
