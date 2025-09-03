import datetime

now = datetime.datetime.now

string = input("입력 : ")

if "안녕" in string:
    print("안녕하세요.")
elif "지금 몇 시" in string:
    print("지금은 {}시 {}분 입니다.".format(datetime.datetime.now().hour, datetime.datetime.now().minute))
else:
    print(string)