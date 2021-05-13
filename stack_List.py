class stack:
    def __init__(self):
        self.List = []
    def push(self,value):
        self.List.append(value)
    def pop(self):
        self.List.pop()
    def isEmpty(self):
        if len(self.List)==0:
            print("The Stack is empty")
        else:
            print("The Stack is not empty")
    def printStack(self):
        print(self.List)
    def peek(self):
        top = len(self.List)
        print(self.List[top-1])

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