dictionary ={
      "키A" : "값A"
    , "키B" : "값B"
    , "키C" : "값C"
}

print("딕셔너리의 items() 함수")
print("items() : ", dictionary.items())
print()

print("딕셔너리의 items()와 반복문 조합")
for key, element in dictionary.items():
    print(f"dictionary[{key}] = {element}")