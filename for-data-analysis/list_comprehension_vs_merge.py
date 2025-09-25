list_1 = ['사과', '바나나', '복숭아']
list_2 = ['주스', '잼', '통조림']

# 일반적인 리스트.
pairs_n = []
for fruit in list_1:
    for product in list_2:
        pairs_n.append((fruit, product))
print("pairs_n = ", pairs_n)

# 리스트 컴프리헨션.
pairs_c = [(fruit, product) for fruit in list_1 for product in list_2]
print("pairs_c = ", pairs_c)
