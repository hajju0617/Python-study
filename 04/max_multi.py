max_value = 0

for i in range(1, 100 // 2 + 1):
    j = 100 - i

    if max_value < i * j:
        max_value = i * j

print(f"곱셈이 최대가 되는 경우 : {i} * {j} = {max_value}")