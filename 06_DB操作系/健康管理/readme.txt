cd ~/dev/Python-Tool-Box/06_DB操作系/健康管理
cd %HOMEDRIVE%%HOMEPATH%\dev\Python-Tool-Box\06_DB操作系\健康管理

# 初期導入時
pip install matplotlib
pip install jpholiday

# ドキュメント表示
python -m pydoc manageHelth

# 全件取得
python manageHelth.py
python manageHelth.py -m select_all

# 登録(登録日時をシステム日付で設定)
python manageHelth.py -m save -w 68.2

# 登録(日付指定)
python manageHelth.py -m save -t 176.7 -w 68.2 -d '2020/06/27'
python manageHelth.py -m save -w 68.2 -d '2020/11/14'
python manageHelth.py -m save -w 68.2 -d '2020/05/01'

# キーで検索
python manageHelth.py -m select_key -i 20

# キーで削除
python manageHelth.py -m del_key -i 22

# キーで更新
python manageHelth.py -m upd_key -t 176.5 -w 68.2 -i 90
python manageHelth.py -m upd_key -w 68.2 -i 109

# BMI計算・表示
python manageHelth.py -m show_bmi -w 68.2

# 最大体重だった日のデータを表示
python manageHelth.py -m max_weight

# 最小体重だった日のデータを表示
python manageHelth.py -m min_weight

# 年月指定でグラフ表示
python manageHelth.py -m show_monthly_graph -tym 202011

# 指定期間指定でグラフ表示
python manageHelth.py -m show_term_graph -from 2020-11-09 -to 2020-12-08

# 直近１ヶ月でグラフ表示
python manageHelth.py -m show_past_month_graph -to 2020-12-14
python manageHelth.py -m show_past_month_graph

# TODO
# 平均体重をグラフタイトルに表示・・・2021/01/08実装済み
# 最軽量、最重量の体重をグラフタイトルに表示・・・2021/01/08実装済み
# Web(Flask)化・・・2021/01/10実装済み
# グラフをブラウザに表示(Flask化)・・・2021/01/11実装済み

# 毎月の平均体重の推移

# 共通処理のテスト
cd lib
python -m unittest

# WEB起動
python web_health_manage.py

# 一覧表示
http://localhost:5002/


以上