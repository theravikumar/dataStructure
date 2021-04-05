class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Circular_singly_LinkedList:
    def __init__(self):
        self.head = None
         
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:
                break
    def insert_CSLL_Node(self,position,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
        else:
            if position == 0:
                newNode.next = self.head
                self.head = newNode
                tempNode = newNode.next
                while tempNode.next != newNode.next:
                    
                    tempNode = tempNode.next
                tempNode.next = newNode
            else:
                count = 0
                tempNode = self.head
                while tempNode.next != self.head:
                    count = count+1
                    tempNode = tempNode.next
                if count == position-1:
                    nodeCount = self.head
                    while nodeCount.next!=self.head:
                        
                        nodeCount = nodeCount.next
                    nodeCount.next = newNode
                    newNode.next = self.head
                else:
                    count1 = 0
                    nodeCount1 = self.head
                    while count1< position-1:
                        count1 = count1+1
                        nodeCount1 = nodeCount1.next
                    newNode.next = nodeCount1.next
                    nodeCount1.next = newNode

           
CircularsinglyLinkedList = Circular_singly_LinkedList()
CircularsinglyLinkedList.insert_CSLL_Node(0,1)
CircularsinglyLinkedList.insert_CSLL_Node(1,2)
CircularsinglyLinkedList.insert_CSLL_Node(2,3)
CircularsinglyLinkedList.insert_CSLL_Node(3,5)
CircularsinglyLinkedList.insert_CSLL_Node(0,6)
# CircularsinglyLinkedList.addNode(2)
print ([Node.value for Node in CircularsinglyLinkedList])