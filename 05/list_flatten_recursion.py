def flatten(list_data):
    result_list = []

    for item in list_data:
        if type(item) == list:
            result_list += flatten(item)        # 재귀호출.
        else:
            result_list.append(item)

    return result_list

list_data = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 list : ", list_data)
print("변환된 list : ", flatten(list_data))