base = float(input("밑변의 길이를 입력해주세요. : "))
height = float(input("높이의 길이를 입력해주세요. : "))

hypo = (base ** 2 + height ** 2) ** (1 / 2)

print(f"빗변의 길이는 {hypo} 입니다.")