# All sorts of traversal in a binary tree

class Tree:
    def __init__(self,value=None,parent=None,left=None,right=None,child=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.child = child

def DFS_inorder(rootnode):
    if not rootnode:
        return None
    inorder (rootnode.left)
    print(rootnode.value)
    inorder (rootnode.right)

def DFS_preorder(rootnode):
    if not rootnode:
        return None
    print(rootnode.value)
    preorder(rootnode.left)
    preorder(rootnode.right)

def DFS_postorder(rootnode):
    if not rootnode:
        return None
    postorder(rootnode.left)
    postorder(rootnode.right)
    print(rootnode.value)

def BFS(rootnode):
    if not rootnode:
        return None
    q = []
    q.append(rootnode)
    while(q):
        tmp = q[0]
        q.pop(0)
        print(tmp.value)
        if tmp.left:
            q.append(tmp.left)
        if tmp.right:
            q.append(tmp.right)

root = Tree(10)  
root.left = Tree(11)  
root.left.left = Tree(7)  
root.right = Tree(9)  
root.right.left = Tree(15)  
root.right.right = Tree(8)  

BFS(root)