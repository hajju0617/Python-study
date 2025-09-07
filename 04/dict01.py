dictionary = {
    "name" : "건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "사과", "소금"],
    "origin" : "필리핀"
}

print("dictionary : ", dictionary)
print("dictionary['name'] : ", dictionary["name"])
print("dictionary['type'] : ", dictionary["type"])
print("dictionary['ingredient'] : ", dictionary["ingredient"])
print("dictionary['ingredient'][0] : ", dictionary["ingredient"][0])
print("dictionary['ingredient'][2] : ", dictionary["ingredient"][2])
print("dictionary['origin'] : ", dictionary["origin"])
print()

print("dictionary['name']의 value 변경")
dictionary["name"] = "말린 망고"
print("dictionary['name'] : ", dictionary["name"])
print()
print("dictionary 새로운 키, 새로운 값")
dictionary["price"] = 55000
print("dictionary : ", dictionary)

print()
print("del 키워드를 사용해서 특정 키 제거하기")
del dictionary["ingredient"]
print("dictionary : ", dictionary)
