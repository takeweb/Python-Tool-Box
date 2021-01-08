import datetime, sqlite3

def select_all_for_graph(db_file, from_date, to_date):
    """
    データベースからグラフ用データ取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                      strftime('%d', date(regist_datetime))
                    , weight 
                FROM health 
                WHERE regist_datetime BETWEEN ? AND ?
                ORDER BY regist_datetime'''
    to_date = get_to_date_for_search(to_date)
    curs.execute(select, (from_date, to_date))
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def save(db_file, regist_datetime, height, weight, bmi):
    """
    データベースに保存
    """
    conn = sqlite3.connect(db_file)
    conn.execute('''CREATE TABLE IF NOT EXISTS health(
                          data_id INTEGER PRIMARY KEY AUTOINCREMENT
                        , regist_datetime TEXT
                        , height FLOAT
                        , weight FLOAT
                        , bmi FLOAT)''')
    ins = ('INSERT INTO health(regist_datetime, height, weight, bmi) VALUES(?, ?, ?, ?)')
    conn.execute(ins, (regist_datetime, height, weight, bmi))
    conn.commit()
    conn.close()

def select_all(db_file):
    """
    データベースから全件取得
    """
    conn = sqlite3.connect(db_file)
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
                    regist_datetime'''
    curs.execute(select)
    rows = curs.fetchall()
    curs.close()
    conn.close()
    return rows

def select_max_seq(db_file, table_name):
    """
    最大シーケンス取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = 'SELECT seq FROM sqlite_sequence WHERE name = ?'
    curs.execute(select, (table_name,))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return row[0]

def select_by_key(db_file, data_id):
    """
    キーで１件取得
    """
    conn = sqlite3.connect(db_file)
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
    conn.close()
    return row

def select_max_weight(db_file):
    """
    最大体重だった日のデータを取得
    """
    conn = sqlite3.connect(db_file)
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
    conn.close()
    return row

def select_min_weight(db_file):
    """
    最小体重だった日のデータを取得
    """
    conn = sqlite3.connect(db_file)
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
    conn.close()
    return row

def select_ave_weight_term(db_file, from_date, to_date):
    """
    指定期間の平均体重を取得
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    select = '''SELECT
                    AVG(weight) 
                FROM
                    health
                WHERE
                    regist_datetime BETWEEN ? AND ?
            '''
    to_date = get_to_date_for_search(to_date)
    curs.execute(select, (from_date, to_date))
    row = curs.fetchone()
    curs.close()
    conn.close()
    return round(row[0], 1)

def select_max_weight_term(db_file, from_date, to_date):
    """
    指定期間の最大体重を取得
    """
    conn = sqlite3.connect(db_file)
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

def select_min_weight_term(db_file, from_date, to_date):
    """
    指定期間の最小体重を取得
    """
    conn = sqlite3.connect(db_file)
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

def update_by_key(db_file, data_id, regist_datetime, height, weight, bmi):
    """
    キーで更新
    """
    conn = sqlite3.connect(db_file)
    upd = ('''UPDATE health 
                SET
                      regist_datetime = ?
                    , height = ? 
                    , weight = ? 
                    , bmi = ?
                WHERE data_id = ?''')
    conn.execute(upd, (regist_datetime, height, weight, bmi, data_id))
    conn.commit()
    conn.close()

def delete_by_key(db_file, data_id):
    """
    キーで削除
    """
    conn = sqlite3.connect(db_file)
    delete = ('DELETE FROM health WHERE data_id = ?')
    conn.execute(delete, (data_id, ))
    conn.commit()
    conn.close()

def get_to_date_for_search(to_date):
    """
    日付で検索する場合、時刻部分がが「00:00:00」で検索されることになるので、
    TO日時は23:59:59を加算してSQLへバインドする
    """
    dt_to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
    dt_to_date = dt_to_date + datetime.timedelta(hours=23, minutes=59)
    to_date = dt_to_date.strftime('%Y-%m-%d %H:%M')

    return to_date