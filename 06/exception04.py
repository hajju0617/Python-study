list_numbers = [52, 273, 32, 72, 100]

try:
    number_input = int(input('정수 입력 : '))
    print(f'{number_input}번째 요소 : {list_numbers[number_input]}')
    예외.발생

except ValueError as ve:
    print('정수만 입력해 주세요.')
    print('ve = ', ve)
    print('type(ve) = ', type(ve))
except IndexError as ie:
    print('리스트의 인덱스를 벗어났음.')
    print('ie = ', ie)
    print('type(ie) = ', ie)
except Exception as e:
    print('예상치 못한 예외가 발생.')
    print('e = ', e)
    print('type(e) = ', type(e))