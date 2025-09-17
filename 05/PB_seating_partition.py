minSeatCapacity = 2
maxSeatCapacity = 10
totalPeople = 100

memo = {}

def func(remainingPeople, seatedPeople):
    key = str([remainingPeople, seatedPeople])

    if key in memo:
        return memo[key]
    if remainingPeople < 0:
        return 0
    if remainingPeople == 0:
        return 1
    count = 0
    for i in range(seatedPeople, maxSeatCapacity + 1):
        count += func(remainingPeople - i, i)
    memo[key] = count
    return count

print(func(totalPeople, minSeatCapacity))