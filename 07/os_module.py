import os

print('현재 운영체제 : ', os.name)
print('현재 폴더 : ', os.getcwd())
print('현재 폴더 내부의 요소 : ', os.listdir())
print()

# 디렉토리 변경.
os.chdir("C:/Python-study/07")

# 폴더 생성
os.mkdir('folder')
# 폴더 삭제 (빈폴더인 경우에만 삭제 가능)
os.rmdir('folder')

# 파일 생성
with open('original.txt', 'w') as file:
    file.write('None')
# 파일 이름 변경 (기존, 변경)
os.rename('original.txt', 'new.txt')

# 파일 제거
os.remove('new.txt')    # os.unlink('new.txt')  -> remove(), unlink()는 이름만 다를뿐. 서로 같은 함수임.

# 시스템 명령어 실행.
print('-- 시스템 명령어 실행 --')
os.system('dir')
