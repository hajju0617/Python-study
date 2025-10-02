import sys

# 명령 매개변수 출력.
print('sys.argv = ', sys.argv)
print()

# 컴퓨터 환경과 관련된 정보 출력.
print('sys.getwindowsversion() = ', sys.getwindowsversion())
print('sys.copyright = ', sys.copyright)
print('sys.version = ', sys.version)

sys.exit()