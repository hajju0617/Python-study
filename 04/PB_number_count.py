list_num = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]
dictionary = {}

for i in list_num:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(f"사용된 숫자의 종류는 {len(dictionary)}개")
print("dictionary : ", dictionary)