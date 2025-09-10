limit = 10000
i = 1
sum_value = 0

while sum_value < limit:
    i += 1
    sum_value += i
print(f"{i}를 더할 때 {limit}를 넘으며 그때의 값은 {sum_value}임.")