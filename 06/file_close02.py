import os
os.chdir("C:/Python-study/06")

try:
    file = open("info.txt", 'w')

    예외발생

except:
    print("오류가 발생!")


print('파일이 제대로 닫혔는지 확인.')
print('file.closed : ', file.closed)