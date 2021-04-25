# Python3 program to construct tree using 
# inorder and postorder traversals 
 
# Helper function that allocates 
# a new node 
class newNode:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None
 
# Recursive function to construct binary 
# of size n from Inorder traversal in[] 
# and Postorder traversal post[]. Initial 
# values of inStrt and inEnd should be 
# 0 and n -1. The function doesn't do any 
# error checking for cases where inorder 
# and postorder do not form a tree 
def buildUtil(In, post, inStrt, inEnd, pIndex):
     
    # Base case 
    if (inStrt > inEnd): 
        return None
 
    # Pick current node from Postorder traversal 
    # using postIndex and decrement postIndex 
    node = newNode(post[pIndex[0]]) 
    pIndex[0] -= 1
 
    # If this node has no children 
    # then return 
    if (inStrt == inEnd): 
        return node 
 
    # Else find the index of this node 
    # in Inorder traversal 
    iIndex = search(In, inStrt, inEnd, node.data) 
 
    # Using index in Inorder traversal, 
    # construct left and right subtress 
    node.right = buildUtil(In, post, iIndex + 1, 
                                  inEnd, pIndex) 
    node.left = buildUtil(In, post, inStrt, 
                        iIndex - 1, pIndex) 
 
    return node
 
# This function mainly initializes index 
# of root and calls buildUtil() 
def buildTree(In, post, n):
    pIndex = [n - 1] 
    return buildUtil(In, post, 0, n - 1, pIndex)
 
# Function to find index of value in 
# arr[start...end]. The function assumes 
# that value is postsent in in[] 
def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if (arr[i] == value): 
            break
    return i
 
# This funtcion is here just to test 
def preOrder(node):
    if node == None: 
        return
    print(node.data,end=" ")
    preOrder(node.left) 
    preOrder(node.right)
 
# Driver code 
if __name__ == '__main__':
    In = ['p','m','n','x','y','z']
    post = ['p','n','m','y','z','x'] 
    n = len(In)
 
    root = buildTree(In, post, n) 
 
    print("Preorder of the constructed tree :") 
    preOrder(root)
 
# This code is contributed by PranchalK