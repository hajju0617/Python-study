try:
    user_input_num = int(input("정수 입력 : "))
    print("원의 반지름 : ", user_input_num)
    print("원의 둘레 : ", 2 * 3.14 * user_input_num)
    print("원의 넓이 : ", 3.14 * user_input_num * user_input_num)
except:
        print("정수만 입력해 주세요.")