numbers = [1, 2, 3, 4, 5, 6]
reversed_num = reversed(numbers)

print("reversed_num : ", reversed_num)
print("첫 번째 : ", next(reversed_num))
print("두 번째 : ", next(reversed_num))
print("세 번째 : ", next(reversed_num))
print("네 번째 : ", next(reversed_num))
print("다섯 번째 : ", next(reversed_num))
print("여섯 번째 : ", next(reversed_num))

print('----')
reversed_num = reversed(numbers)
for i in reversed_num:
    print(f'i = {i}')