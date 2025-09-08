from abc import ABC, abstractmethod
import math

class Shape(ABC):                   # 추상 클래스.
    @abstractmethod
    def area(self):                 # 추상 메서드.
        pass

class Circle(Shape):                # 서브 클래스1
    def __init__(self, radius):
        self.radius = radius
    def area(self):                 # 추상 메서드 구현.
        return math.pi * self.radius ** 2

class Rectangle(Shape):             # 서브 클래스2
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):                 # 추상 메서드 구현.
        return self.width * self.height
    

# Circle 객체 생성 및 면적 계산.
circle = Circle(5)
print("Circle Area = {:.3f}".format(circle.area()))

 # Rectangle 객체 생성 및 면적 계산.
rectangle = Rectangle(4, 6)
print("Rectangle Area = ", rectangle.area())