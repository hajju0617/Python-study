class Queue:
    def __init__(self):
        self.list = []
    def enqueue(self, item):
        self.list.append(item)
    def dequeue(self):
        return self.list.pop(0)
    def __str__(self):
        return f'Queue = ({self.list})'
    
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)
print('-----------')
print('dequeue = ', queue.dequeue())
print(queue)
print('dequeue = ', queue.dequeue())
print(queue)
print('dequeue = ', queue.dequeue())
print(queue)