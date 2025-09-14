def print_n_times(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print("키워드 매개변수 사용 X")
print_n_times("123", "abc", "가나다", 3)
print()
print("키워드 매개변수 사용 O")
print_n_times("123", "abc", "가나다", n = 3)