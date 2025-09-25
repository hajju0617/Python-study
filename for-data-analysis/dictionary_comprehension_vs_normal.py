# 일반적인 딕셔너리
squares = {}
for i in range(10 + 1):
    squares[i] = i ** 2
print("squares = ", squares)

# 딕셔너리 컴프리헨션.
squares = {i: i ** 2 for i in range(10 + 1)}
print("squares = ", squares)