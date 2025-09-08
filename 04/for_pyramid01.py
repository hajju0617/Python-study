for i in range(1, 10):
    for j in range(0, i):
        print("*", end="")  # end="" : 줄 바꿈 없앰. (print 기본값: end="\n" (줄바꿈))
    print()

print()

output = ""
for i in range(1, 10):
    for j in range(0, i):
        output += "*"
    output += "\n"
print(output)

print()
for i in range(1, 10):
    print("*" * i)
