class CustomException(Exception):
    def __init__(self):
        super().__init__()
        print('커스텀 예외 클래스 생성')
    def __str__(self):
        return '예외 발생'
raise CustomException