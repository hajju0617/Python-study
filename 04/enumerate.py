list = ["요소A", "요소B", "요소C"]

print("단순 출력")
print(list)
print()

print("enumerate() 함수로 출력")
print(enumerate(list))
print()

print("반복문과 조합")
for i, value in enumerate(list):
    print(f"{i}번째 요소는 {value}임.")