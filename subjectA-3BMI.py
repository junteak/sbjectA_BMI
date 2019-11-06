'''

subjectA-3

'''

print('BMI計算アプリ')

height_m = float(input('身長は? cm : ')) / 100
weight_kg = float(input('体重は? kg : '))


def result(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    print(f'あなたのBMIは{bmi:.2f}です。')
    if bmi < 18.50:
        print('痩せています。')

    if bmi >= 18.50 and bmi < 25.00:
        print('普通体型です。')

    if bmi >= 25.00 and bmi < 30.00:
        print('ぽっちゃり体型です。肥満度1')

    if bmi >= 30.00 and bmi < 35.00:
        print('太り気味です。肥満度2')

    if bmi >= 35.00 and bmi < 40.00:
        print('ハッキリ言ってデブです。肥満度3')

    if bmi > 40.00:
        print('危険です。肥満度4')


if height_m <= 0:
    print('正しい値を入力してください。')

elif weight_kg <= 0:
    print('正しい値を入力してください。')

else:
    result(weight_kg, height_m)
