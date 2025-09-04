list_of_list = [
      [1, 2, 3]
    , [4, 5, 6]
    , [7, 8, 9]
]
print("list_of_list 출력")
print("list_of_list : ", list_of_list)

print("list_of_list를 for문 하나로 출력")
for list in list_of_list:
    print(list)
print()

print("list_of_list를 이중 for문으로 출력.")
for list in list_of_list:
    for element in list:
        print(element)