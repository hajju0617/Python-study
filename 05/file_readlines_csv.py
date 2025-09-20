import os
os.chdir("C:/Python-study/05")

with open("info.txt", "r", encoding="utf-8") as file:
    for line in file:
        (name, height, weight) = line.strip().split(", ")

        # 데이터가 문제없는지 확인.
        if (not name) or (not height) or (not weight):
            continue

        bmi = int(weight) / (int (height) / 100 ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        print('\n'.join([
            f"이름 : {name}"
            , f"키 : {height}"
            , f"몸무게 : {weight}"
            , f"BMI : {bmi}"
            , f"결과 : {result}"
        ]))
        print()
