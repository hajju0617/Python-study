i = 0

while True:
    print(f"{i}번째 반복임.")
    i += 1

    input_text = input("종료? (y/n) : ")
    if input_text in ["y", "Y"]:
        print("반복을 종료함.")
        break