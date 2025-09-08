import random

list = ["rock", "paper", "scissors"]
a = random.choice(list)
b = random.choice(list)

print("a : ", a)
print("b : ", b)

if a == b:
    print("a, b : tie")
elif (a == "rock" and b == "scissors") or (a == "paper" and b == "rock") or (a == "scissors" and b == "paper"):
    print("a win")
else:
    print("b win")