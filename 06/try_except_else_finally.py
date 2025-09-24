try:
    number_input = int(input("정수 입력 : "))

    print("원의 반지름 : ", number_input)
    print("원의 둘레 : ", 2 * 3.14 * number_input)
    print("원의 넓이 : ", 3.14 * number_input * number_input)
except:
    print("정수만 입력해야됨.")
else:
    print("예외가 발생하지 않았음.")
finally:
    print("일단 프로그램이 종료되었음.")