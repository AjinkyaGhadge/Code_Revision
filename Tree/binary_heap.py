class BinaryHeap:

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0
        
    def _position_node(self,heapsize):
        while heapsize//2 > 0:
            if self.heaplist[heapsize//2]>self.heaplist[heapsize]:
                self.heaplist[heapsize//2],self.heaplist[heapsize] = self.heaplist[heapsize],self.heaplist[heapsize//2]
            heapsize = heapsize//2 
    
    def insert(self,data):
        self.heaplist.append(data)
        self.currentsize+=1
        self._position_node(self.currentsize)

    def _position_root(self,i):
        while i*2 <= self.currentsize:
            if i * 2 + 1 > self.currentsize:
                loc = i * 2
            else:
                if min(self.heaplist[i*2],self.heaplist[i*2+1]) == self.heaplist[i*2]:
                    loc = i*2
                else:
                    loc = i*2+1
            if self.heaplist[i] > self.heaplist[loc]:
                self.heaplist[i],self.heaplist[loc] = self.heaplist[loc],self.heaplist[i]
            i = loc
    
    def pop(self):
        data = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize-=1
        self.heaplist.pop()
        self._position_root(1)
        return data

    def heapfromlist(self,arr:list):
        i = len(arr)//2
        self.currentsize = len(arr)
        self.heaplist = [0]+arr
        while i > 0:
            self._position_root(i)
            i-=1

heapvals = BinaryHeap()
heapvals.heapfromlist([10,5,8,2,3])

print(heapvals.pop())
print(heapvals.pop())
print(heapvals.pop())
print(heapvals.pop())
print(heapvals.pop())

'''
Output:

2
3
5
8
10
'''