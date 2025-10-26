import math

# Python에서 private 변수는 '__(변수명)'으로 사용.
class Circle:
    def __init__(self, radius):
        self.__radius = radius      # .__radius : 외부에서 접근하지 못하는 private 변수.
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    # getter, setter (Python에서 getter가 없으면 setter를 만들 수 없음.)
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)
print(f'원의 둘레 : {circle.get_circumference()}')
print(f'원의 넓이 : {circle.get_area()}')
print()

print('__radius에 접근.')
print(f'circle.get_radius = {circle.get_radius()}')
print()

circle.set_radius(5)
print('setter를 이용해서 반지름 변경 (10 -> 5)')
print(f'원의 둘레 : {circle.get_circumference()}')
print(f'원의 넓이 : {circle.get_area()}')