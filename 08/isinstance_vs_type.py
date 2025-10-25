class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass
student = Student()

print(f'isinstance(student, Human) : {isinstance(student, Human)}')     # isinstance() : 상속 관계까지 확인함.
print(f'type(student) == Human : {type(student) == Human}')             # type() : 상속 관계 확인 X