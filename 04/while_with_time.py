import time

number = 0

# time.time() : 유닉스 타임 구함. (유닉스 타임이란? UTC 기준 몇 초가 지났는지를 정수로 나타낸 것.)
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print(f"5초 동안 {number}번 반복했음.")