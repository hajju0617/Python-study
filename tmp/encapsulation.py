class Car:
    def __init__(self, speed=0):
        self.__speed = speed            # speed를 private으로 선언한것.

    def get_speed(self):                # getter 메서드.
        return self.__speed
    
    def set_speed(self, speed):         # setter 메서드.
        self.__speed = speed

car = Car()
print("현재 Speed = ", car.get_speed()) # getter 메서드를 통한 접근.

car.set_speed(60)                       # setter 메서드를 통한 접근.
print("업데이트 된 Speed = ", car.get_speed())