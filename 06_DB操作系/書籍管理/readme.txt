
# ISBN10用のチェックデジット算出
python manageBook.py -m 10 -i 4-7981-0912

# ISBN13用のチェックデジット算出
python manageBook.py -m 13 -i 978-4-7980-2655

＃Cコード解読
python manageBook.py -m c -c 3055

# 登録
python manageBook.py -m save -ib ISBN978-4-04-893073-4 -n "JavaScript Primer" -o 3800 -p "株式会社 ドワンゴ"
python manageBook.py -m save -ib ISBN978-4-87311-783-6 -n "初めてのJavaScript" -o 3200 -p "オライリー・ジャパン"

# 全件取得
python manageBook.py -m select_all
python manageBook.py

# キー指定１件取得
python manageBook.py -m read_key -i 1

# キー指定で１件更新
python manageBook.py -m upd_key -i 1 -n "JavaScript Primer2" -sa "株式会社 KADOKAWA" -a "azu, Suguru Inatomi"
python manageBook.py -m upd_key -i 2 -a "Ethan Brown" -t "武舎 広幸, 武舎 るみ" -sa "オーム社"
python manageBook.py -m upd_key -i 2 -tg "JavaScript" -r "備考"

# キー指定１件削除
python manageBook.py -m del_key -i 1
