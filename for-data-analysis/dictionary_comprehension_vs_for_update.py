scores = {'김철수': 45, '이영희': 38, '박지성': 49, '최민수': 30, '정수정': 42}

# 일반적인 딕셔너리
percentage_scores_old = {}
for name, score in scores.items():
    percentage_scores_old[name] = ((score) / 50) * 100
print("일반적인 딕셔너리 percentage_scores_old = ", percentage_scores_old)

# 딕셔너리 컴프리헨션.
percentage_scores_new = {name: ((score) / 50) * 100 for name, score in scores.items()}
print("딕셔너리 컴프리헨션 percentage_scores_new = ", percentage_scores_new)