import math

# Python에서 private 변수는 '__(변수명)'으로 사용.
class Circle:
    def __init__(self, radius):
        self.__radius = radius      # .__radius : 외부에서 접근하지 못하는 private 변수.
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
circle = Circle(10)
print(f'원의 둘레 : {circle.get_circumference()}')
print(f'원의 넓이 : {circle.get_area()}')
print()

print('__radius에 접근.')
print(f'circle.__radius = {circle.__radius}')