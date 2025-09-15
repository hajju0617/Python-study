def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

print("1! = ", factorial(1))
print("2! = ", factorial(2))
print("5! = ", factorial(5))
print("10! = ", factorial(10))
