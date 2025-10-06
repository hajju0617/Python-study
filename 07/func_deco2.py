from functools import wraps

def test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):   # 가변 매개변수, 키워드 가변 매개변수를 가져옴.
        print('인사 시작')
        function(*args, **kwargs)
        print('인사 종료')
    return wrapper

@test
def hello():
    print('hello')
hello()