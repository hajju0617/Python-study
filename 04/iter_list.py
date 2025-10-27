list_a = [1, 2, 3]
# next(list_a)
iterator_a = iter(list_a)
print(type(iterator_a))

print(next(iterator_a))
print(next(iterator_a))
print(next(iterator_a))
# print(next(iterator_a))