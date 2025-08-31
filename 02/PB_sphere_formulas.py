pi = 3.141592
r = float(input("구의 반지름을 입력하세요. : "))

volume = 4 / 3 * pi * r ** 3
surface_area = 4 * pi * r ** 2

print("구의 부피는 {:.3f} 입니다.".format(volume))
print("구의 겉넓이는 {:.3f} 입니다.".format(surface_area))