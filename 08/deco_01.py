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
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if (value <= 0):
            raise TypeError('길이는 자연수여야함.')
        self.__radius = value

print(f'데코레이터를 사용한 getter, setter')
circle = Circle(10)
print(f'현재 원의 반지름 = {circle.radius}')
circle.radius = 5
print(f'변경된 원의 반지름 = {circle.radius}')
print()

print(f'강제로 예외 발생.')
circle.radius = -1