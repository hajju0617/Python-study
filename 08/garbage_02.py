class Test:
    def __init__(self, name):
        self.name = name
        print(f'{self.name} - 생성되었음.')
    def __del__(self):
        print(f'{self.name} - 파괴되었음.')

A = Test('A')
B = Test('B')
C = Test('C')