# 일반적인 리스트 생성.
numbers_a = []
for i in range(5):
    numbers_a.append(i)
print("일반적인 리스트 방식으로 생성한 numbers = ", numbers_a)

# 리스트 컴프리헨션을 사용한 리스트 생성.
numbers_b = [i for i in range(5)]
print("리스트 컴프리헨션을 사용해서 생성한 numbers = ", numbers_b)