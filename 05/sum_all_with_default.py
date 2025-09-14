def sum_all(start = 1, end = 100, step = 1):
    total = 0
    for i in range(start, end + 1, step):
        total += i
    return total

print("1 ~ 100까지 10씩 증가한 수들의 합 : ", sum_all(step= 10))
print("1 ~ 100까지 5씩 증가한 수들의 합 : ", sum_all(step= 5))
print("1 ~ 1000까지 2씩 증가한 수들의 합 : ", sum_all(end = 1000, step= 2))