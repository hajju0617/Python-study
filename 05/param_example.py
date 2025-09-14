def func(a, b = 200, c = 300):
    print("a + b + c = ", a + b + c)

print("기본 형태")
func(10, 20, 30)
print("키워드 매개변수로 모든 매개변수를 지정.")
func(a = 10, b = 20, c = 30)
print("키워드 매개변수로 모든 매개변수를 무작위로 지정")
func(c = 30, a = 10, b = 20)
print("키워드 매개변수로 일부 매개변수만 지정.")
func(a = 10, c = 30)