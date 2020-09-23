cd /Users/oishi/develop/python3/Python-Tool-Box/06_DB操作系/健康管理

# ドキュメント表示
python -m pydoc manageHelth

# 全件取得
python manageHelth.py
python manageHelth.py -m read_all

# 登録
python manageHelth.py -m save -t 176.7 -w 80.5 -d '2020/06/27'

# 登録(登録日時をシステム日付で)
python manageHelth.py -m save -w 79.9

# キーで検索
python manageHelth.py -m read_key -i 20

# キーで削除
python manageHelth.py -m del_key -i 22

# キーで更新
python manageHelth.py -m upd_key -t 176.8 -w 80.5 -i 22

# 指定期間指定でグラフ表示
python manageHelth.py -m graph -f 2019-10-01 -to 2020-07-31
python manageHelth.py -m graph -f 2020-04-01 -to 2020-04-30
python manageHelth.py -m graph -f 2020-05-01 -to 2020-05-31
python manageHelth.py -m graph -f 2020-06-01 -to 2020-06-30
python manageHelth.py -m graph -f 2020-07-01 -to 2020-07-31
