calculations = [
    (10, '+', 5),
    (20, '-', 8),
    (6, '*', 7),
    (15, '/', 3),
    (8, '/', 0),
    (12, '%', 5)
]

elementary_arithmetic = ['+', '-', '*', '/']

print('계산 결과 :')
for a, op, b in calculations:
    if op not in elementary_arithmetic:
        print('잘못된 연산자 입니다.')
        continue
    if op == '/' and b == 0:
        print('0으로 나눌 수 없습니다.')
        continue
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        result = a / b
    print(f'{a} {op} {b} = {result}')
    