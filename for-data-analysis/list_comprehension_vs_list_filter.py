numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 일반적인 리스트
even_numbers_n =[]
for num in numbers:
    if num % 2 == 0:
        even_numbers_n.append(num)
print("even_numbers_n = ", even_numbers_n)

# 리스트 컴프리헨션
even_numbers_c = [num for num in numbers if num % 2 == 0]
print("even_numbers_c = ", even_numbers_c)