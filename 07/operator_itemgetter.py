# operator 모듈의 itemgetter() 함수를 가져옴.
from operator import itemgetter

# books = [  {"제목" : "혼자 공부하는 파이썬"
#          ,  "가격" : 18000}, 
#            {"제목" : "혼자 공부하는 머신러닝 + 딥러닝"
#          ,  "가격" : 26000} , 
#            {"제목" : "혼자 공부하는 자바스크립트"
#          ,  "가격" : 24000}
#         ]


# print("가장 저렴한 책")
# # key 매개변수를 통해 비교 기준을 지정.
# print(min(books, key = itemgetter('가격')))
# print()
# print("가장 비싼 책")
# print(max(books, key = itemgetter('가격')))

data = [ ("가나다", 3), ("abc", 1), ("123", 2) ]

# 두 번째 요소(숫자)를 기준으로 정렬
sorted_data = sorted(data, key=itemgetter(1))
print(sorted_data)