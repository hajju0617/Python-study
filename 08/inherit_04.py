class CustomException(Exception):
    def __init__(self, message, value):
        super().__init__()
        self.message = message
        self.value = value
    def __str__(self):
        return self.message
    def print(self):
        print('[오류 정보]')
        print(f'메시지 : {self.message}')
        print(f'값 : {self.value}')

try:
    raise CustomException('커스텀 예외 발생', 404)
except CustomException as e:
    e.print()