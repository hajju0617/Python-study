dictionary = {
    "name" : "가나다",
    "type" : "한글"
}

key = input("접근하려는 키 : ")

if dictionary.get(key) == None:
    print("존재하지 않는 키에 접근하였음. ", f"dictionary.get({key}) : ", dictionary.get(key))
else:
    print(f"dictionary.get({key}) : ", dictionary.get(key))