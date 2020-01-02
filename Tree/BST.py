class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def lookup(self,data,parent=None):
        if data<self.data:
            if self.left is None:
                return None,None
            else:
                return self.left.lookup(data,self)
        elif data>self.data:
            if self.right is None:
                return None,None
            else:
                return self.right.lookup(data,self)
        else:
            return self,parent

    def delete(self,data):
        a , b = self.lookup(data)
        if (a == None):
            print("data not found")
            return False
        elif (b == None and a!= None):
            if a.left == None and a.right == None:
                a.data = None

            if a.left == None and a.right != None:
                a = a.right
            if a.left != None and a.right == None:
                a = a.left
            if a.left != None and a.right!=None:
                c = a.right
                t = c
                while(c.left!=None and c.right!=None):
                    t = c
                    c = c.left
                t.left = None
                a.data = c.data
            return True
        else:
            if a.data < b.data:
                loc = 0
            elif a.data > b.data:
                loc = 1
            
            if a.left == None and a.right == None:
                if loc == 0:
                    b.left = None
                elif loc == 1:
                    b.right = None
            if a.left == None and a.right != None:
                if loc == 0:
                    b.left = a.right
                elif loc == 1:
                    b.right = a.right
            if a.left != None and a.right == None:
                if loc == 0:
                    b.left = a.left
                elif loc == 1:
                    b.right = a.left
            if a.left != None and a.right!=None:
                c = a.right
                while(c.left!=None and c.right!=None):
                    temp = c
                    c = c.left
                temp.left = None
                a.data = c.data
            return True
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end = ' ')
        
        if self.right is not None:
            self.right.inorder()
    def preorder(self):
        print(self.data, end = ' ')
       
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()
    def postorder(self):
        if self.right is not None:
            self.right.postorder()
        print(self.data, end = ' ')
        
        if self.left is not None:
            self.left.postorder()
    
    def levelorder(self):
        q = list()
        if self.data is None:
            return False
        if self.data is not None:
            q.append(self)
        while(len(q)!=0):
            temp = q.pop()
            print(temp.data, end= " ")
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)

                
root = Node(10)
root.insert(6)
root.insert(11)
root.insert(7)
root.insert(5)
root.inorder() #DFS
print(" ")
root.preorder() #DFS
print(" ")
root.postorder() #DFS
print(" ")
root.levelorder() #BFS