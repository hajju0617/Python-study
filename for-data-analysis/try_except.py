try:
    result = 10 / 0
    print('result = ', result)
except ZeroDivisionError:
    print('0으로 나눌 수 없음.')