def get_dataset_stats(values):
    return min(values), max(values), sum(values) / len(values)

data = [12, 8, 21, 17, 5, 32, 14]
minimum, maximum, average = get_dataset_stats(data)
print(f'최솟값 : {minimum}, 최댓값 : {maximum}, 평균값 : {average}')