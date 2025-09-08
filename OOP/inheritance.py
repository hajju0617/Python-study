class Animal:               # 슈퍼 클래스 (부모 클래스)
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    

class Cat(Animal):          # 서브 클래스1 (자식 클래스)
    def speak(self):
        return f"{self.name} says Meow"
    
class Dog(Animal):          # 서브 클래스2 (자식 클래스)
    def speak(self):
        return f"{self.name} says Woof"
    
cat = Cat("Whiskers")
print("cat.speak() : ", cat.speak())

dog = Dog("Buddy")
print("dog.speak() : ", dog.speak())