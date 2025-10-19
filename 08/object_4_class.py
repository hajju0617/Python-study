# 클래스 선언.
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
    
    def to_string(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'
students = [
    Student('김민준', 92, 88, 95, 78), 
    Student('이서연', 75, 98, 85, 90), 
    Student('박도현', 88, 70, 92, 85), 
    Student('정하윤', 95, 90, 78, 92), 
    Student('최은우', 65, 82, 70, 95), 
    Student('홍지아', 80, 95, 88, 82)
]

print('이름', '총점', '평균', sep='\t')
for student in students:
    print(student.to_string())