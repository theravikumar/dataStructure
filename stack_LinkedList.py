class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class stack:
    def __init__(self):
        self.head = None
    def push(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def pop(self):
        if self.head is None:
            print("the stack is empty. Pop operation cannot be performed")
        else:
            self.head = self.head.next 
    def isEmpty(self):
        if self.head is None:
            print("stack is empty")
        else:
            print("stack is not empty")
    def peek(self):
        if self.head is None:
            print("the stack is empty")
        else:
            print(self.head.value)
    def printStack(self):
        tempNode=self.head
        tempList=[]
        while tempNode:
            tempList.append(tempNode.value)
            tempNode = tempNode.next
        print(tempList[::-1])

Stack = stack()
Stack.push(5)
Stack.printStack()
Stack.pop()
Stack.isEmpty()
for i in range(10):
    Stack.push(i)
Stack.isEmpty()
Stack.peek()
Stack.printStack()
               