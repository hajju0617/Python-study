key_list = ["name", "hp", "mp", "level"]
value_list = ["전사", 200, 50, 10]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)