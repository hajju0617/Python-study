dictionary = {
    "name" : "가나다",
    "type" : "한글"
}

key = input("접근하려고 하는 키 : ")

if key in dictionary:
    print(f"dictionary[{key}] : ", dictionary[key])
else:
    print(key + "는 존재하지 않음.")