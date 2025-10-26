class Student:
    # 클래스 변수.
    count = 0       
    students = []

    # 클래스 함수.
    '''
    @classmethod는 클래스 자체를 첫 번째 인자(cls)로 받는 메서드.
    즉, Student.print()를 호출하면 Python이 내부적으로
    Student.print(Student) <- 이렇게 호출함.
    (cls는 Student 클래스 자체를 참조하게 됨)
    '''
    @classmethod
    def print(cls):
        print('------- 학생 목록 -------')
        print(f'이름\t총점\t평균')
        for student in cls.students:
            print(str(student))
        print('------- ------- -------')

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return f'{self.name}\t{self.get_sum()}\t{self.get_average()}'


Student('김민준', 92, 88, 95, 78) 
Student('이서연', 75, 98, 85, 90) 
Student('박도현', 88, 70, 92, 85) 
Student('정하윤', 95, 90, 78, 92) 
Student('최은우', 65, 82, 70, 95) 
Student('홍지아', 80, 95, 88, 82)
Student('박아현', 97, 92, 88, 95)
Student('서준서', 45, 52, 72, 78)
Student('연하진', 97, 98, 88, 95)
Student('구지연', 76, 97, 94, 90)

Student.print()