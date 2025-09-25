import urllib.request

# URL 연결 관리
with urllib.request.urlopen('https://raw.githubusercontent.com/jaehwachung/Data-Analysis-with-Open-Source/refs/heads/main/Chapter%203/students.csv')as response:    
    data = response.read( ).decode('utf-8')
print(data)

# urlopen() 메서드로 해당 URL에 HTTP GET 요청을 보냄.