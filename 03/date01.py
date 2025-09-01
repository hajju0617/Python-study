# 모듈 import
import datetime

# 현재 날짜 및 시간
now = datetime.datetime.now()

print("현재 날짜 및 시간")
print("format을 이용한 날짜 및 시간 출력 : {}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))
print(f"f-문자열을 이용한 날짜 및 시간 출력 : {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초")