list_a = [0, 1, 2, 3, 4, 5]
print("list_a : ", list_a)

del list_a[1]
print("del list_a[1]한 결과 : ", list_a)

list_a.pop(2)
print("list_a.pop(2)한 결과 : ", list_a)
print()

list_b = [0, 1, 2, 3, 4, 5, 6]
print("list_b : ", list_b)
del list_b[1:5]
print("del list_b[1:5]한 결과 : ", list_b)

list_c = [0, 1, 2, 3, 4, 5, 6]
print("list_c : ", list_c)
del list_c[2:]
print("del list_c[2:]한 결과 : ", list_c)