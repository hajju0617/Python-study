class Student:
    count = 0       # 클래스 변수.
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        print(f'{Student.count}번째 학생이 생성되었음.')

students = [
    Student('김민준', 92, 88, 95, 78), 
    Student('이서연', 75, 98, 85, 90), 
    Student('박도현', 88, 70, 92, 85), 
    Student('정하윤', 95, 90, 78, 92), 
    Student('최은우', 65, 82, 70, 95), 
    Student('홍지아', 80, 95, 88, 82)
]
print()
print(f'현재 생성된 총 학생 수는 {Student.count}명.')