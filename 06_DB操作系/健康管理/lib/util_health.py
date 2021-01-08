import matplotlib.pyplot as plt

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

def hantei_bmi(bmi):
    """
    BMI判定
    """
    if bmi < 18.5:
        result = "痩せ型"
    elif bmi >= 18.5 and bmi < 25:
        result = "標準体型"
    elif bmi >= 25 and bmi < 30:
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
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
    plt.plot(day_list, weight_list)
    plt.grid(color='0.8')
    plt.title(title)
    plt.xlabel("days")
    plt.ylabel("weight(kg)")
    plt.show()

def show_bmi(height, weight, target_weight, before=0):
    # BMIと適正体重を計算
    bmi = calc_bmi(height, weight)
    suitable_weight = calc_suitable_weight(height)

    result_bmi = hantei_bmi(bmi)
    result_suitable_weight = round((suitable_weight - weight) * -1, 2)
    hantei_suitable_weight = 'あと' if result_suitable_weight > 0 else '達成'
    result_target_weight = round((target_weight - weight) * -1, 2)
    hantei_target_weight = 'あと' if result_target_weight > 0 else '達成'
    result_ratio = round((before - weight) * -1, 2)

    print("BMI(Body Mass Index): " + str(bmi) + " / 判定: " + result_bmi)
    print("適正体重:" + str(suitable_weight) + "kg" + " / " + hantei_suitable_weight + ": " + str(result_suitable_weight) + "kg！")
    print("目標体重:" + str(target_weight)   + "kg" + " / " + hantei_target_weight   + ": " + str(result_target_weight)   + "kg！")
    if before != 0:
        print("前日比　:" + str(result_ratio)   + "kg")
    return bmi
