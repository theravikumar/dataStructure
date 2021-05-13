class queue:
    def __init__(self):
        self.List = []
    def enqueue(self,value):
        self.List.append(value)
    def dequeue(self):
        del self.List[0]
    def peek(self):
        print(self.List[0])
    def isEmpty(self):
        if len(self.List)==0:
            print("the queue is empty")
        else:
            print("the queue is not empty")
    def printQueue(self):
        print(self.List)

Queue = queue()
Queue.enqueue(5)
Queue.printQueue()
Queue.dequeue()
Queue.isEmpty()
for i in range(10):
    Queue.enqueue(i)
Queue.isEmpty()
Queue.peek()
Queue.printQueue()