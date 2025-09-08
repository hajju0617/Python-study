class Animal:                   # 슈퍼 클래스 (부모 클래스)
    def sound(self):
        pass

class Dog(Animal):              # 자식 클래스1 (서브 클래스)
    def sound(self):
        return "멍멍"
    
class Cat(Animal):              # 자식 클래스2 (서브 클래스)
    def sound(self):
        return "야옹"
    
class Cow(Animal):              # 자식 클래스3 (서브 클래스)
    def sound(self):
        return "음메"
    

def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
cow = Cow()
print(f"강아지 소리 : {make_sound(dog)}")
print(f"고양이 소리 : {make_sound(cat)}")
print(f"소 소리 : {make_sound(cow)}")