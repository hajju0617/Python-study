students_scores =[
      ('김철수', 85, 92, 78)
    , ('이영희', 92, 88, 95)
    , ('박지민', 75, 83, 90)
]

for name, database, python, cloud in students_scores:
    average = (database + python + cloud) / len(students_scores)
    print(f'{name}의 평균 점수 : {average:.1f}')