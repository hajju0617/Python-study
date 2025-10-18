# 딕셔너리를 리턴하는 함수.
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return f"{student['name']}\t{student_get_sum(student)}\t{student_get_average(student)}"

students = [
    create_student('김민준', 92, 88, 95, 78), 
    create_student('이서연', 75, 98, 85, 90), 
    create_student('박도현', 88, 70, 92, 85), 
    create_student('정하윤', 95, 90, 78, 92), 
    create_student('최은우', 65, 82, 70, 95), 
    create_student('홍지아', 80, 95, 88, 82)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))