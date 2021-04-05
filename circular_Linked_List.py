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

    def delete_SLL_Node(self,position):
        if position == 0:
            delNode = self.head
            while delNode.next != self.head:
                delNode = delNode.next
            self.head = self.head.next
            delNode.next = self.head
        else:
            count = 0
            tempNode = self.head

            while tempNode.next != self.head:
                count = count+1
                temp = tempNode
                tempNode = tempNode.next
            if count == position-1:
                temp.next.next = None
                temp.next = self.head
            else:
                i = 0
                delNode = self.head
                
                while i<position:
                    i = i+1
                    preNode = delNode
                    delNode = delNode.next
                preNode.next = delNode.next
                delNode.next = None

    def search_CSLL_value(self,value):
        testNode = self.head
        position = 0
        while testNode:
            if testNode.value == value:
                return(position)
            position = position + 1
            testNode = testNode.next
        return ("value is not stored")
    def update_CSLL_Node(self,position,value):
        if position == 0:
            self.head.value = value
        else:

            i = 0
            updateNode = self.head
            
            while i<position:
                i = i+1
                
                updateNode = updateNode.next
            updateNode.value = value

                

           
CircularsinglyLinkedList = Circular_singly_LinkedList()
CircularsinglyLinkedList.insert_CSLL_Node(0,1)
CircularsinglyLinkedList.insert_CSLL_Node(1,2)
CircularsinglyLinkedList.insert_CSLL_Node(2,3)
CircularsinglyLinkedList.insert_CSLL_Node(3,5)
CircularsinglyLinkedList.insert_CSLL_Node(3,6)
# CircularsinglyLinkedList.addNode(2)
print ([Node.value for Node in CircularsinglyLinkedList])
CircularsinglyLinkedList.delete_SLL_Node(4)
print ([Node.value for Node in CircularsinglyLinkedList])
print(CircularsinglyLinkedList.search_CSLL_value(6))
CircularsinglyLinkedList.update_CSLL_Node(3,9)
print ([Node.value for Node in CircularsinglyLinkedList])