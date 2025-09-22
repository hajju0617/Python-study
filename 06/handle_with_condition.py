user_input = input("정수 입력 : ")

# 사용자 입력값이 숫자로만 구성되어 있다면.
if user_input.isdigit():
    num = int(user_input)
    print("원의 반지름 : ", num)
    print("원의 둘레 : ", 2 * 3.14 * num)
    print("원의 넓이 : ", 3.14 * num * num)
else:
    print("정수만 입력해 주세요.")