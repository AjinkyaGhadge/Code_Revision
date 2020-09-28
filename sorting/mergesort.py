class Node:
    def __init__(self, v=0,nxt=None):
        self.val = v
        self.next = nxt

class Solution:

    def merge(self,l=None,r=None):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l.val,r.val = r.val,l.val
        head = pre = l
        l = l.next
        while(l and r):
            if l.val > r.val:
                pre.next = r
                tmp = r
                r = r.next
                tmp.next = l
            else:
                l=l.next
            pre = pre.next
        if r:
            pre.next = r
        return head

# n1 = Node(8)
# n2 = Node(5,n1)
# n3 = Node(4,n2)
# n4 = Node(2,n3)

# m  = Node(10)
# m0 = Node(9,m)
# m1 = Node(7,m0)
# m2 = Node(6,m1)
# m3 = Node(3,m2)
# m4 = Node(1,m3)

# l = n4
# r = m4

# k = Solution()
# j = k.merge(l,r)

# while j:
#     print(j.val)
#     j = j.next