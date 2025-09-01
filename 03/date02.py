# 모듈 import
import datetime

# 현재 날짜 및 시간
now = datetime.datetime.now()

if now.hour < 12:
    print(f"현재 시각은 {now.hour}시로 오전입니다.")
if now.hour > 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))