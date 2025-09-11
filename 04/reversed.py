list_a = [1, 2, 3, 4, 5]
list_a_reversed = reversed(list_a)

print("reversed() 사용.")
print("reversed(list_a) : ", list_a_reversed)
print("list(reversed(list_a)) : ", list(list_a_reversed))
print()

print("reversed()와 반복문")
for i in reversed(list_a):
    print("-", i)