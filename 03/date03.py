# 모듈 import
import datetime

# 현재 날짜 및 시간
now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print(f"이번 달은 {now.month}월로 봄입니다.")
if 6 <= now.month <= 8:
    print(f"이번 달은 {now.month}월로 여름입니다.")
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다.".format(now.month))
if (now.month == 12 or 1 <= now.month <= 2):
    print("이번 달은 {}월로 겨울입니다.".format(now.month))