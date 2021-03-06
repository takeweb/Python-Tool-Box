import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from io import BytesIO
import urllib
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')

def calc_bmi(cm_height, weight):
    """
    BMIを算出

    Parameters
    ----------
    cm_height : fload
        身長(cm)
    weight : float
        体重(kg)

    Returns
    -------
    bmi : float
        BMI値
    """
    # BMI ＝ 体重kg ÷ (身長m)の２の階乗
    m_height = cm_height / 100
    bmi = round(weight / m_height ** 2, 2)
    return bmi

def calc_suitable_weight(cm_height):
    """
    適正体重を算出
    """
    m_height = cm_height / 100
    suitableWeight = round(m_height ** 2 * 22, 1)
    return suitableWeight

def judge_bmi_jp(bmi):
    """
    BMI判定(日本肥満学会の判定基準)
    """
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi >= 18.5 and bmi < 25:
        result = "普通体重"
    elif bmi >= 25 and bmi < 30:
        result = "肥満(1度)"
    elif bmi >= 30 and bmi < 35:
        result = "肥満(2度)"
    elif bmi >= 35 and bmi < 40:
        result = "肥満(3度)"
    else:
        result = "肥満(4度)"
    return result

def judge_bmi_who(bmi):
    """
    BMI判定(世界保健機関(WHO)の判定基準)
    """
    if bmi < 16:
        result = "痩せすぎ"
    elif bmi >= 16 and bmi <= 16.99:
        result = "痩せ"
    elif bmi >= 17 and bmi <= 18.49:
        result = "痩せぎみ"
    elif bmi >= 18.5 and bmi <= 24.99:
        result = "普通体重"
    elif bmi >= 25 and bmi <= 29.99:
        result = "前肥満"
    elif bmi >= 30 and bmi <= 34.99:
        result = "肥満(1度)"
    elif bmi >= 35 and bmi <= 39.99:
        result = "肥満(2度)"
    else:
        result = "肥満(3度)"
    return result

def disp_graph(rows, title):
    """
    グラフ表示
    """
    day_list = []
    weight_list = []

    for row in rows:
        day_list.append(row[0])
        weight_list.append(row[1])
    _, ax = plt.subplots(figsize=(9.0, 7.0))
    ax.set_title(title)
    ax.plot(day_list, weight_list)
    plt.grid(color='0.8')
    plt.xlabel("days")
    plt.ylabel("weight(kg)")
    plt.show()

def save_graph(rows, title, file_name):
    """
    グラフ画像を保存
    """
    day_list = []
    weight_list = []

    for row in rows:
        day_list.append(row[0])
        weight_list.append(row[1])

    fig = Figure(figsize=(9.0, 7.0))
    ax = fig.add_subplot()
    ax.set_title(title)
    ax.grid(color='0.8')
    # ax.xlabel("days")
    # ax.ylabel("weight(kg)")
    ax.plot(day_list, weight_list)
    
    canvas = FigureCanvasAgg(fig)
    canvas.print_figure(file_name)
    buf = BytesIO()
    canvas.print_png(buf)
    img_data = urllib.parse.quote(buf.getvalue())

    return img_data

def save_graph2(rows, title, file_name):
    """
    グラフ画像を保存
    """
    day_list = []
    weight_list = []

    for row in rows:
        day_list.append(row[0])
        weight_list.append(row[1])

    _, ax = plt.subplots(figsize=(9.0, 7.0))
    ax.set_title(title)

    plt.plot(day_list, weight_list)

    plt.grid(color='0.8')
    plt.xlabel("days")
    plt.ylabel("weight(kg)")

    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    return img_data

def get_result_list(height, weight, target_weight, before=0):
    # BMIと適正体重を計算
    bmi = calc_bmi(height, weight)
    suitable_weight = calc_suitable_weight(height)

    result_bmi = judge_bmi_jp(bmi)
    result_suitable_weight = round((suitable_weight - weight) * -1, 2)
    hantei_suitable_weight = 'あと' if result_suitable_weight > 0 else '達成'
    result_target_weight = round((target_weight - weight) * -1, 2)
    hantei_target_weight = 'あと' if result_target_weight > 0 else '達成'
    result_ratio = round((before - weight) * -1, 2)

    result_list = []
    result_list.append("BMI(Body Mass Index): " + str(bmi) + " / 判定: " + result_bmi)
    result_list.append("適正体重:" + str(suitable_weight) + "kg" + " / " + hantei_suitable_weight + ": " + str(result_suitable_weight) + "kg！")
    result_list.append("目標体重:" + str(target_weight)   + "kg" + " / " + hantei_target_weight   + ": " + str(result_target_weight)   + "kg！")
    if before != 0:
        result_list.append("前日比　:" + str(result_ratio)   + "kg")
    return result_list