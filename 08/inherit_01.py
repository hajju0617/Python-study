# 부모 클래스
class Parent:
    def __init__(self):
        self.value = "테스트"
        print('Parent 클래스의 __init()__ 메서드가 호출되었음.')
    def test(self):
        print('Parent 클래스의 test() 메서드.')

# 자식 클래스
class Child(Parent):
    def __init__(self):
        super().__init__()  # 부모 클래스의 __init__() 함수를 호출.
        print('Child 클래스의 __init()__ 메서드가 호출되었음.')
child = Child()
child.test()
print(f'child.value = {child.value}')