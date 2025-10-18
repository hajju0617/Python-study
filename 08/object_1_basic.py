students = [
    {
        "name": "김민준",
        "korean": 92,
        "math": 88,
        "english": 95,
        "science": 78
    },
    {
        "name": "이서연",
        "korean": 75,
        "math": 98,
        "english": 85,
        "science": 90
    },
    {
        "name": "박도현",
        "korean": 88,
        "math": 70,
        "english": 92,
        "science": 85
    },
    {
        "name": "정하윤",
        "korean": 95,
        "math": 90,
        "english": 78,
        "science": 92
    },
    {
        "name": "최은우",
        "korean": 65,
        "math": 82,
        "english": 70,
        "science": 95
    },
    {
        "name": "홍지아",
        "korean": 80,
        "math": 95,
        "english": 88,
        "science": 82
    }
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_avg = score_sum / 4
    print(student["name"], score_sum, score_avg, sep="\t")