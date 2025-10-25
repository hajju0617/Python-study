class Student:
    def __init__(self):
        pass

student = Student()

print(f'isinstance(student, Student) : {isinstance(student, Student)}')
print(f'type(student) == Student : {type(student) == Student}')     # 상속을 사용하면 다르게 동작함.

'''
isinstance(인스턴스, 클래스) : 인스턴스가 해당 클래스로 만들어졌는가? True 또는 False 리턴.
'''