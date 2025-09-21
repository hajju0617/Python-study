books = [  {"제목" : "혼자 공부하는 파이썬"
         ,  "가격" : 18000}
         , {"제목" : "혼자 공부하는 머신러닝 + 딥러닝"
         ,  "가격" : 26000}
         , {"제목" : "혼자 공부하는 자바스크립트"
         ,  "가격" : 24000
         }
        ]
print("원본 books")
print("books = ", books)
print()
print("가격 오름차순 정렬")
books.sort(key = lambda book : book["가격"])
for book in books:
    print("book = ", book)
print()
print("가격 내림차순 정렬")
books.sort(key = lambda book : book["가격"], reverse=True)
for book in books:
    print("book = ", book)




def test(f):
    f = [4, 5, 6]

e = [1, 2, 3]
test(e)
print(e)