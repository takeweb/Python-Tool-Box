cd /Users/oishi/develop/python3/Python-Tool-Box/06_DB操作系/パスワード管理

# 全件取得
python managePw.py
python managePw.py -m read_all

# 登録
python managePw.py -m save -p 'Take0014!' -c 1

# カレントパスワードを取得
python managePw.py -m get_current_pw

# カレントパスワードを指定したキーに変更
python managePw.py -m change_current_pw -i 1 -c 1

# 次のパスワード候補を取得
python managePw.py -m get_next_pws

# キーで検索
python managePw.py -m read_key -i 12

# キーで更新
python managePw.py -m upd_key -i 12 -p 'Take0014/'
python managePw.py -m upd_key -i 12 -p 'Take0014/' -c 1

# キーで削除
python managePw.py -m del_key -i 22


# ドキュメント表示
python -m pydoc managePw

# DBへ直接接続
sqlite3 passwd.db