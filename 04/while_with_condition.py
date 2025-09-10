list = [1, 2, 2, 1, 2, 2, 1]
value = 2

while value in list:
    list.remove(value)
    print("값을 삭제함. -> ", value)
print(list)