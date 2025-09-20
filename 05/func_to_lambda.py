power = lambda x: x * x
under_3 = lambda x: x < 3

list_input = [1, 2, 3, 4, 5]

print("-- map 함수 --")
output = map(power, list_input)
print("map(power, list_input) = ", output)
print("map(power, list_input) = ", list(output))
print()

print("-- filter 함수 --")
output2 = filter(under_3, list_input)
print("filter(under_3, list_input) = ", output2)
print("filter(under_3, list_input) = ", list(output2))