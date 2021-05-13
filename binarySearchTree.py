class BST:
    def __init__(self,value = None):
        self.value = value
        self.leftNode = None
        self.rightNode = None
    def insertNode(self,value):
        if self.value is None:
            self.value = value
        elif self.value == value:
            return
        elif value < self.value:
            if self.leftNode:
                self.leftNode.insertNode(value)
                
            else:
                self.leftNode = BST(value)
                
        else:
            if self.rightNode:
                self.rightNode.insertNode(value)
                
            else:
                self.rightNode = BST(value)
                
    def inOrderTravelsal(self):
        
        if self.leftNode is not None:
            self.leftNode.inOrderTravelsal()
        if self.value is not None:
            print(self.value)
        if self.rightNode is not None:
            self.rightNode.inOrderTravelsal()
    def postOrderTravelsal(self):
        
        if self.leftNode is not None:
            self.leftNode.postOrderTravelsal()
        if self.rightNode is not None:
            self.rightNode.postOrderTravelsal()        
        if self.value is not None:
            print(self.value)

    def preOrderTravelsal(self):
        if self.value is not None:
            print(self.value)        
        if self.leftNode is not None:
            self.leftNode.preOrderTravelsal()
        if self.rightNode is not None:
            self.rightNode.preOrderTravelsal()  

    def nodeExists(self,value):
        if value == self.value:
            print("node exist")
        elif value < self.value:
            if self.leftNode:
                self.leftNode.nodeExists(value)
            else:
                print("node does not exist")
        else:
            if self.rightNode:
                self.rightNode.nodeExists(value)
            else:
                print("node does not exist")
    def minNodeValue(self):
        if self.leftNode:
            self.leftNode.minNodeValue()
        else:
            print("minmum node value in tree: ",self.value)
    def maxNodeValue(self):
        if self.rightNode:
            self.rightNode.maxNodeValue()
        else:
            print("maximum node value in tree: ",self.value)
    def deleteNode(self,value):
        Set = False
        if value == self.value:
            Set = True
            
        elif value < self.value:
            if self.leftNode:
                
                self.leftNode.deleteNode(value)
                return
                
            else:
                Set =  False
        else:
            if self.rightNode:
                
                self.rightNode.deleteNode(value)
                return
            else:
                Set = False
        if Set == True:
            delete = self
            
            if self.rightNode:
                
                tempNode = self.rightNode
                
                while tempNode.leftNode:
                    
                    tempNode = tempNode.leftNode
                    
                delete.value = tempNode.value
                
                tempNode.value = None
            elif self.leftNode:
                delete = self.leftNode
            else:
                delete.value = None
        else:
            print("Node cannot be deleted")
            

tree = BST()

tree.insertNode(15)
tree.insertNode(8)
tree.insertNode(5)
tree.insertNode(23)
tree.insertNode(12)
tree.insertNode(26)
tree.insertNode(17)
tree.inOrderTravelsal()
print("-----------")
tree.postOrderTravelsal()
print("------------")
tree.preOrderTravelsal()
print("------------")
tree.nodeExists(23)
tree.nodeExists(34)
tree.minNodeValue()
tree.maxNodeValue()
tree.deleteNode(26)
tree.preOrderTravelsal()
