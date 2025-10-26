class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'
    
    def __eq__(self, value):    # equal
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):    # not equal
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):    # greater than
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):    # greater than or equal
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):    # less than
        return self.get_sum() < value.get_sum()
    def __le__(self, value):    # less than or equal
        return self.get_sum() <= value.get_sum()
    
students = [
    Student('김민준', 92, 98, 95, 78), 
    Student('이서연', 75, 98, 85, 90), 
    Student('박도현', 88, 70, 92, 85), 
    Student('정하윤', 95, 90, 78, 92), 
    Student('최은우', 65, 82, 70, 95), 
    Student('홍지아', 80, 95, 88, 82)
]
student_a = Student('김민준', 92, 98, 95, 78)
student_b = Student('이서연', 75, 98, 85, 90)

print(f'student_a == student_b : {student_a == student_b}')
print(f'student_a != student_b : {student_a != student_b}')
print(f'student_a > student_b : {student_a > student_b}')
print(f'student_a >= student_b : {student_a >= student_b}')
print(f'student_a < student_b : {student_a < student_b}')
print(f'student_a <= student_b : {student_a <= student_b}')