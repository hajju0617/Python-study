dictionary = {
    "name" : "가나다",
    "type" : "한글"
}
print("dictionary 요소 제거 이전 : ", dictionary)

del dictionary["name"]
del dictionary["type"]

print("dictionary 요소 제거 이후 : ", dictionary)