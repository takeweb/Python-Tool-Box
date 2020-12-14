cd /Users/oishi/develop/python3/Python-Tool-Box/06_DB操作系/TSAパスワード管理

# 登録
python manageTsaPw.py -m save -p 000

# 全表示
python manageTsaPw.py -m get_all

# 次のパスワード候補を取得
python manageTsaPw.py -m get_next_pw

# 連続登録
python manageTsaPw.py -m series_save -p 99

# 削除
python manageTsaPw.py -m del_pw -p 17123456789

# ドキュメント表示
python -m pydoc managePw

# DBへ直接接続
sqlite3 passwd.db