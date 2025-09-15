dictionary = {
      1 : 1
    , 2 : 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]            # 메모되어 있는 값을 바로 return.
    else:
        total = fibonacci(n - 1) + fibonacci(n - 2)
        dictionary[n] = total           # 메모.
        return total

print("fibonacci(1) = ", fibonacci(1))
print("fibonacci(2) = ", fibonacci(2))
print("fibonacci(3) = ", fibonacci(3))
print("fibonacci(4) = ", fibonacci(4))
print("fibonacci(5) = ", fibonacci(5))
print("fibonacci(25) = ", fibonacci(25))
print("fibonacci(50) = ", fibonacci(50))