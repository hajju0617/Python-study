number = int(input("정수 입력 : "))

if number % 2 == 0:
    print(f"{number}은/는 짝수입니다.")
if number % 2 == 1:
    print("{}은/는 홀수입니다.".format(number))