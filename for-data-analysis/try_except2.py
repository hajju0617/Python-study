try:
    number = int(input('정수 입력 : '))
    result = 10 / number
except ValueError:
    print('유효한 숫자를 입력하세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없음.')