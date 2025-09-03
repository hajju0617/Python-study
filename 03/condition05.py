# 모듈 import
import datetime

# 현재 날짜 및 시간
now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("현재 계절은 봄입니다.")
elif 6 <= now.month <= 8:
    print("현재 계절은 여름입니다.")
elif 9 <= now.month <= 11:
    print("현재 계절은 가을입니다.")
else:
    print("현재 계절은 겨울입니다.")