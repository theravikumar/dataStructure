class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class queue:
    def __init__(self):
        self.head=None
    def enqueue(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = newNode
    def dequeue(self):
        if self.head is None:
            print("dequeue operation cannot be performed. queue is empty")
        else:
            self.head = self.head.next
    def peek(self):
        if self.head is None:
            print("the queue is empty")
        else:
            print(self.head.value)
    def isEmpty(self):
        if self.head is None:
            print("the queue is empty")
        else:
            print("the queue is not empty")
    def printQueue(self):
        tempNode = self.head
        tempList =[]
        while tempNode:
            tempList.append(tempNode.value)
            tempNode = tempNode.next
        print(tempList)

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