def generator_test():
    print("함수 호출")
    yield "test"

print("A 통과")
generator_test()

print("B 통과")
generator_test()
print(generator_test())     # 제너레이터 함수는 제너레이터를 리턴함.