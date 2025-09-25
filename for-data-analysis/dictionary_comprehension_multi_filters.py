city_population = {
      '서울' : 957, '부산' : 339, '인천' : 294, '대구' : 242, '광주' : 145
    , '대전' : 147, '울산' : 114, '세종' : 36, '수원' : 115, '창원' : 103
    , '고양' : 105, '용인' : 108, '성남' : 94
}
large_cities = {city: pop for city, pop in city_population.items() if pop >= 200}       # 딕셔너리의 .items() 메서드는 딕셔너리의 각 항목을 (키, 값) 튜플의 리스트로 반환함.
# 1. for city, pop in city_population.items()
# 2. if pop >= 200
# 3. city: pop
print("인구 200만 명 이상의 도시 (large_cities) = ", large_cities)

large_short_name_cities = {city: pop for city, pop in city_population.items() if pop >= 300 and '산' in city}
# 1. for city, pop in city_population.items()
# 2. if pop >= 300 and '산' in city
# 3. city: pop
print("인구 300만 명 이상의 '산' 글자가 포함된 도시 (large_short_name_cities) = ", large_short_name_cities)