counter = 0

def fibonacci(n):
    print(f"fibonacci({n})를 구함.")
    global counter
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci(10)
print("===========")
print(f"fibonacci(10)을 계산하기 위해 실행한 덧셈 횟수는 {counter}번임.")