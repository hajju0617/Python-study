import random
import os
os.chdir("C:/Python-study/05")

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w", encoding="utf-8") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        heigth = random.randrange(140, 200)
        file.write(f"{name}, {heigth}, {weight}\n")

