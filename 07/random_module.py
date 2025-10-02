import random

# 0.0 <= x < 1.0 (리턴 타입 : float)
print('random.random() = ', random.random())

# uniform(min, max) : 범위 사이의 임의의 값을 리턴 (float)
print('random.uniform(10, 20) = ', random.uniform(10, 20))

# randrange() : 지정한 값 사이의 값을 리턴 (int)
# randrange(max) : 0~max 사이의 값을 리턴, randrange(min, max) : min~max 사이의 값을 리턴.
print('random.randrange(10) = ', random.randrange(10))

# choice(list) : list 내부의 요소를 랜덤으로 1개 선택해서 리턴.
print('random.choice([1, 2, 3, 4, 5]) = ', random.choice([1, 2, 3, 4, 5]))

# shuffle(list) : list 내부의 요소를 랜덤하게 섞음.
list = [1, 2, 3, 4, 5]
print('list = ', list)
random.shuffle(list)
print('list = ', list)

# sample(list, k = 숫자) : 리스트의 요소 중 k개를 list로 리턴.
print('random.sample([1, 2, 3, 4, 5], k 3) = ', random.sample([1, 2, 3, 4, 5], k = 3))