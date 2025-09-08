

n = int(input("1층 별의 개수 : "))

if n % 2 == 0:                      # K : 몇 줄 찍을지
    K = n // 2
else:
    K = n // 2 + 1

for i in range(1, K + 1):
    s = K - i + 1                   # s : 공백의 개수 (*을 출력할 위치)
    t = n - (2 * (K - i))           # t : * 개수.
    tri = ""
    for j in range(1, s):
        tri += " "
    for k in range(s, s + t):
        tri += "*"
    print(tri)