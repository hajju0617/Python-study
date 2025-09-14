def sum_all(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

print("1 ~ 100까지의 합 : ", sum_all(1, 100))
print("50 ~ 100까지의 합 : ", sum_all(50, 100))
print("1 ~ 1000까지의 합 : ", sum_all(1, 1000))
print("500 ~ 1000까지의 합 : ", sum_all(500, 1000))
print("1 ~ 10000까지의 합 : ", sum_all(1, 10000))