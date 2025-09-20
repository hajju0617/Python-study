def power(item):
    return item * item
def under_3(item):
    return item < 3

list_input = [1, 2, 3, 4, 5]

# map(), filter() 둘다 첫 번째 매개변수는 함수, 두 번째 매개변수는 리스트
print("map 함수")
output = map(power, list_input)
print("map(power, list_input) = ", output)
print("map(power, list_input) = ", list(output))
print()

print("filter 함수")
output2 = filter(under_3, list_input)
print("filter(under_3, list_input) = ", output2)
print("filter(under_3, list_input) = ", list(output2))