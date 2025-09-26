students = [
    ('이지은', 85),
    ('이민수', 92),
    ('박서현', 78),
    ('정준호', 88),
    ('최유진', 95)
]
sorted_students = sorted(students, key = lambda student: student[1])
'''
sorted() 함수
- key 매개변수를 통해 정렬 기준 지정.
- lambda student: student[1] : 리스트의 두 번째 요소(성적)을 기준으로 정렬.
'''
print('-- 성적 오름차순 정렬 --')
for name, score in sorted_students:
    print(f'{name} : {score}')