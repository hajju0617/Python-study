list_numbers = [52, 273, 32, 72, 100]

try:
    number_input = int(input('정수 입력 : '))
    print(f'{number_input}번째 요소 : {list_numbers[number_input]}')
except Exception as exception:
    print('type(exception) = ', type(exception))
    print('발생한 exception = ', exception)