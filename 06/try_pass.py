list_input = ["52", "278", "32", "가나다", "93"]

list_number = []
for item in list_input:
    try:
        float(item)
        list_number.append(item)
    except:
        pass

print(f"{list_input} 내부에 있는 숫자는")
print(f"{list_number} 입니다.")