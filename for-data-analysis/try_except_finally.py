try:
    file = open('data.csv', 'r')
    content = file.read()
    print('content = ', content)
except FileNotFoundError:
    print('파일을 찾을 수 없음.')
finally:
    print('파일 작업 종료.')
    file.close()