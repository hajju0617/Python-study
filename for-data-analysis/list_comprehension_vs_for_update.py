numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 일반적인 리스트
squares_n = []
for num in numbers:
    squares_n.append(num ** 2)
print("squares_n = ", squares_n)

# 리스트 컴프리헨션
squares_c = [num ** 2 for num in numbers]
print("squares_c = ", squares_c)