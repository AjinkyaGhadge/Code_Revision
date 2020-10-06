class TreeList:
    def __init__(self):
        self.data = []
        self.size = 0

    
    def insert_level_order(self,item:int):
        self.data.append(item)
        self.size = self.size +1
    
    def printPreOrder(self,index = 0):
        if index > self.size-1:
            return 
        print(self.data[index])
        self.printPreOrder((2*index)+1)
        self.printPreOrder((2*index)+2)
    
    def printInOrder(self,index = 0):
        if index > self.size-1:
            return
        self.printInOrder(index*2+1)
        print(self.data[index])
        self.printInOrder(index*2+2)

    def printPostOrder(self,index=0):
        if index > self.size-1:
            return
        self.printPostOrder(index*2+1)
        self.printPostOrder(index*2+2)
        print(self.data[index])
    

    def deleteNode(self,index):
        self.data[index] = self.data[self.size-1]
        self.data[self.size-1] = None
    

node = TreeList()
node.insert_level_order(8)
node.insert_level_order(5)
node.insert_level_order(1)
node.insert_level_order(7)
node.insert_level_order(10)
node.insert_level_order(12)

node.printPreOrder()
print(node.data)
