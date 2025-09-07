numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 1, 8, 8, 8, 8, 9, 9, 9, 0, 0]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print("counter : ", counter)