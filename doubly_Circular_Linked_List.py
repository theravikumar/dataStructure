class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Circular_Doubly_LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next
            if tempNode == self.head:
                break
    def insert_Node(self,position,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            newNode.next = newNode
            
        else:
            if position==0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                node = newNode.next
                
                while node.next != newNode.next:
                    node = node.next
                node.next = newNode
            else:
                tempNode = self.head
                count = 0
                while tempNode.next != self.head:
                    count = count+1
                    
                    tempNode = tempNode.next
                
                if count == position-1:
                    
                    node = self.head
                    while node.next!=self.head:
                        
                        node = node.next
                    
                    node.next = newNode
                    
                    newNode.prev = node
                    
                    newNode.next = self.head
                    
                else:
                    count = 0
                    node = self.head
                    while count<position-1:
                        node = node.next
                        count = count + 1
                    newNode.next = node.next
                    node.next.prev = newNode
                    newNode.prev = node
                    node.next = newNode
    def delete_Node(self,position):
        if position == 0:
            node  = self.head
            while node.next != self.head:
                node = node.next
            
            self.head = self.head.next
            node.next = self.head
            self.head.prev = None
        else:
            count = 0
            node = self.head
            while node.next != self.head:
                count = count+1
                preNode = node
                node = node.next
            if count == position-1:
                preNode.next = self.head
                node.pre = None
                node.next = None
            else:
                tempNode = self.head
                count = 0
                while count < position:
                    node = tempNode
                    tempNode = tempNode.next
                    count = count+1
                node.next = tempNode.next
                tempNode.prev = node
    def search_node_value(self,value):
        testNode = self.head
        position = 0
        while testNode:
            if testNode.value == value:
                return(position)
            position = position + 1
            testNode = testNode.next
        return ("value is not stored")
    def update_Node(self,position,value):
        if position == 0:
            self.head.value = value
        else:

            i = 0
            updateNode = self.head
            
            while i<position:
                i = i+1
                
                updateNode = updateNode.next
            updateNode.value = value
    



CircularDoublyLinkedList = Circular_Doubly_LinkedList()
CircularDoublyLinkedList.insert_Node(0,1)
CircularDoublyLinkedList.insert_Node(1,2)
CircularDoublyLinkedList.insert_Node(2,3)
CircularDoublyLinkedList.insert_Node(3,4)
print([node.value for node in CircularDoublyLinkedList])
CircularDoublyLinkedList.insert_Node(2,5)
print([node.value for node in CircularDoublyLinkedList])
CircularDoublyLinkedList.delete_Node(4)
print([node.value for node in CircularDoublyLinkedList])
print(CircularDoublyLinkedList.search_node_value(1))
CircularDoublyLinkedList.update_Node(2,9)
print([node.value for node in CircularDoublyLinkedList])
