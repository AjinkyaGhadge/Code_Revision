"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
        
    def flatten(self, head: 'Node') -> 'Node':
        
        def flatten_dfs(head: 'Node') -> 'Node':
            if not head:
                return None
            nonlocal q
            q.append(head.val)
            flatten_dfs(head.child)
            flatten_dfs(head.next)
        q = []
        if not head:
            return None
        flatten_dfs(head)
        h2 = Node(q[0],None,None,None)
        t = h2
        q.pop(0)
        for i in q:
            tmp = Node(i,None,None,None)
            tmp.prev = t
            t.next = tmp
            t = t.next    
        return h2
        
        