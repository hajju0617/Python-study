list_numbers = [52, 273, 32, 72, 100]

try:
    number_input = int(input('정수 입력 : '))
    print(f'{number_input}번째 요소 : {list_numbers[number_input]}')
except ValueError as ve:
    print('정수만 입력해 주세요.')
    print('ve = ', ve)
except IndexError as ie:
    print('리스트의 인덱스를 벗어났음.')
    print('ie = ', ie)