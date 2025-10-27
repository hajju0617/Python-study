class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()
    def __str__(self):
        return f'Stack({self.list})'
    
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
print('----------')
print('pop() :', stack.pop())
print(stack)
print('pop() :', stack.pop())
print(stack)
print('pop() :', stack.pop())
print(stack)