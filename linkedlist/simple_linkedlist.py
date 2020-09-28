class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

a = Node(3)
b = Node(4,a)
c = Node(5,b)

d = Node()

d.next,d = c,c

print(d.next.value)
