list_a = [3, 32, 52, 63, 79, 36, 23, 5, 92, 83, 43]
print("list_a 정렬 전 : ", list_a)
list_a.sort()                           # 오름차순 정렬 (기본값).
print("list_a 정렬 후(오름차순) : ", list_a)
list_a.sort(reverse=True)               # 내림차순 정렬 (reverse=True).
print("list_a 정렬 후(내림차순) : ", list_a)
