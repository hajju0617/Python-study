import datetime
now = datetime.datetime.now()
print('now = ', now)

# 특정 시간 더하기
after = now + datetime.timedelta(weeks = 1, days = 1, hours=1, minutes=1, seconds=1)
print(after.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))
print()

# 특정 시간 요소 교체.
output = now.replace(year=(now.year + 1))
print(output.strftime('%Y{} %m{} %d{} %H{} %M{} %S{}').format(*'년월일시분초'))
