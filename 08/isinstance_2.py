class Student:
    def study(self):
        print(f'(Student 객체) 파이썬 공부해요.')
class Teacher:
    def teach(self):
        print(f'(Teacher 객체) 학생을 가르침')

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    else:
        person.teach()