def call_10_times(func):
    for i in range(10):
        print_hello()

def print_hello():
    print("안녕 (print_hello() 호출)")

call_10_times(print_hello)