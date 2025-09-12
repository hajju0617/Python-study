list_2d = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
list_flat = []

for i in list_2d:
    if type(i) == list:
        for j in i:
            list_flat.append(j)
    else:
        list_flat.append(i)
print(list_flat)