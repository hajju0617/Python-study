def generator_test():
    print("A 통과")
    yield "A"
    print("B 통과")
    yield "B"
    print("C 통과")
    # yield "C" 없음.

result = generator_test()

print("D 통과")
print(next(result))
print('----------')
print("E 통과")
print(next(result))
print('----------')
print("F 통과")
print(next(result))
print('----------')
# 한 번 더 실행.
# next(result)        # StopIteration 예외 발생.