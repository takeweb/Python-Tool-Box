cd /Users/oishi/develop/python3/Python-Tool-Box/06_DB操作系/健康管理

# 全件取得
python manageHelth.py
python manageHelth.py -m read_all

# 登録
python manageHelth.py -m save -t 176.7 -w 80.5 -d '2020/06/27'

# 登録(登録日時をシステム日付で)
python manageHelth.py -m save -t 176.7 -w 79.9

# キーで検索
python manageHelth.py -m read_key -d '2020/06/28'

# キーで削除
python manageHelth.py -m del_key -d 2020/07/07

# キーで更新
python manageHelth.py -m upd_key -t 176.8 -w 80.5 -d '2020/06/27'

# 指定期間をグラフ表示
python manageHelth.py -m graph -f 2020-07-01 -to 2020-07-31
