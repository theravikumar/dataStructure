class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
class SLinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert_SLL_Node(self,position,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            if position == 0:
                newNode.next = self.head
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
            self.head = self.head.next
        else:

            i = 0
            delNode = self.head
            
            while i<position:
                i = i+1
                preNode = delNode
                delNode = delNode.next
            preNode.next = delNode.next
            delNode.next = None
    def search_SLL_value(self,value):
        testNode = self.head
        position = 0
        while testNode:
            if testNode.value == value:
                return(position)
            position = position + 1
            testNode = testNode.next
        return ("value is not stored")
    def update_SLL_Node(self,position,value):
        if position == 0:
            self.head.value = value
        else:

            i = 0
            updateNode = self.head
            
            while i<position:
                i = i+1
                
                updateNode = updateNode.next
            updateNode.value = value
    
    
        


    

    
    
Single_Linked_List = SLinkedList()
# node1 = Node(1)
# node2 = Node(2)
# Single_Linked_List.head = node1
# node1.next = node2
# Single_Linked_List.tail = node2
Single_Linked_List.insert_SLL_Node(0,0)
Single_Linked_List.insert_SLL_Node(1,1)
Single_Linked_List.insert_SLL_Node(2,2)
Single_Linked_List.insert_SLL_Node(3,3)
Single_Linked_List.insert_SLL_Node(0,4)
Single_Linked_List.insert_SLL_Node(4,8)
print ([Node.value for Node in Single_Linked_List])
Single_Linked_List.delete_SLL_Node(0)
print ([Node.value for Node in Single_Linked_List])
print(Single_Linked_List.search_SLL_value(4))
Single_Linked_List.update_SLL_Node(0,5)
print ([Node.value for Node in Single_Linked_List])


