number = input("정수 입력 : ")
last_character = number[-1]     # [-1] : 끝 값.

if last_character in "02468":
    print(f"{number}은/는 짝수입니다.")
if last_character in "13579":
    print("{}은/는 홀수입니다.".format(number))