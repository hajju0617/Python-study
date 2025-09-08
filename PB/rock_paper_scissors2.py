import random

list = ["rock", "paper", "scissors"]

while True:
    a = random.choice(list)
    b = random.choice(list)
    print("a : ", a)
    print("b : ", b)
    
    if a == b:
        continue
    elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
        print("a win")
        break
    else:
        print("b win")
        break