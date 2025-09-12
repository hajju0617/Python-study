nucleos = input("염기 서열을 입력하세요 : ")

dictionary = {
      "A" : 0
    , "T" : 0
    , "G" : 0
    , "C" : 0
}

for i in nucleos:
    dictionary[i] += 1
for i in dictionary:
    print(f"{i}의 개수 : {dictionary[i]}")