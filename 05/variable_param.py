def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()
print_n_times(5, "가나다", "abc", "123")