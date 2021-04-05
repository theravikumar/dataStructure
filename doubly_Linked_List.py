class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert_node(self,position,value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = None
            newNode.pre = None
            self.head = newNode
        else:
            
            if position == 0:
                 node = self.head
                 node.prev = newNode
                 newNode.next = node
                 self.head = newNode
            else:
                count = 0
                tempNode = self.head
                while tempNode.next:
                    count = count+1
                    tempNode = tempNode.next
                if count == position-1:
                    nodeCount = self.head
                    while nodeCount.next:
                        nodeCount = nodeCount.next
                    nodeCount.next = newNode
                    newNode.prev = nodeCount
                else:
                    node = self.head
                    count = 0
                    while count < position - 1:
                        node = node.next
                        count = count + 1
                    newNode.next = node.next
                    node.next.prev = newNode
                    newNode.prev = node
                    node.next = newNode

    def delete_node(self,position):
        
        if position == 0:
            self.head = self.head.next
            self.head.prev = None
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
            







DoublyLinkedList = Doubly_Linked_List()
DoublyLinkedList.insert_node(0,1)
DoublyLinkedList.insert_node(1,2)
DoublyLinkedList.insert_node(2,3)
DoublyLinkedList.insert_node(3,4)

print([node.value for node in DoublyLinkedList])
DoublyLinkedList.insert_node(3,5)
print([node.value for node in DoublyLinkedList])
DoublyLinkedList.delete_node(4)
print([node.value for node in DoublyLinkedList])
print(DoublyLinkedList.search_node_value(2))
DoublyLinkedList.update_Node(3,9)
print([node.value for node in DoublyLinkedList])