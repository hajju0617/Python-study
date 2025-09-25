numbers = [10, 20, 30, 40, 50, 60, 70]
         # 0   1   2   3   4   5   6
         # -7  -6  -5  -4  -3  -2  -1

subset_a = numbers[0 : 3]       # 끝인덱스의 값은 포함되지 않음.
print("subset_a = ", subset_a)

subset_b = numbers[ : 4]        # 시작 인덱스 생략 가능.
print("subset_b = ", subset_b)

subset_c = numbers[:]           # 시작, 끝 인덱스 둘 다 생략할 경우 전체가 됨.
print("subset_c = ", subset_c)

subset_d = numbers[-3 : ]       # 음수는 뒤에서부터.
print("subset_d = ", subset_d)