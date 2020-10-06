# A Binary Heap is a Binary Tree with the following properties.

# 1) Binary heap is a complete tree (All levels filled besides possibly the last level. The last level has all leaf nodes as left as possible).

# 2) It is either Min Heap or Max Heap. That is the root should always be minimum or maximum respectively.

# For revision use the link https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html
# For how heapify works go to https://www.geeksforgeeks.org/building-heap-from-array/

max = float('inf')
class binaryheap:
    def __init__(self):
        self.heapdata = [max]
        self.heapsize = 0


    def percolate_up(self,index):
        while index // 2 > 0:
            if self.heapdata[index//2] < self.heapdata[index]:
                self.heapdata[index//2],self.heapdata[index] = self.heapdata[index],self.heapdata[index//2]
            index = index // 2
    
    def insert(self,data):
        self.heapdata.append(data)
        self.heapsize+=1
        self.percolate_up(self.heapsize)

    def poptop(self):
        ret_val = self.heapdata[1]
        self.heapdata[1] = self.heapdata[self.heapsize]
        self.heapdata.pop()
        self.heapsize-= 1
        self.percolate_down(1)
        return ret_val
    
    def percolate_down(self,i):
        while(i * 2 <= self.heapsize):
            greater_index = self.greater_index(i)
            self.heapdata[i],self.heapdata[greater_index] = self.heapdata[greater_index],self.heapdata[i]
            i = greater_index
    
    def greater_index(self,i):
        if i*2+1 > self.heapsize:
            return i*2
        else:
            if self.heapdata[i*2] > self.heapdata[i*2+1]:
                return i*2
            else:
                return i*2+1

    def heapify(self,raw_heap):
        self.heapsize = len(raw_heap)
        self.heapdata.extend(raw_heap)
        i = self.heapsize//2
        while i > 0:
            self.percolate_down(i)
            i = i-1
    
    def printHeap(self):
        print("Values in heap are",self.heapdata)

    def clearHeap(self):
        self.heapdata = [max]
        self.heapsize = [0]
        

t = binaryheap()
t.printHeap()
t.insert(10)
t.insert(20)
t.insert(30)
t.insert(15)
t.insert(16)
t.printHeap()
print(t.poptop())
t.printHeap()
t.clearHeap()
t.printHeap()
t.heapify([10,20,30,40,50,60,70])
print(t.poptop())
print(t.poptop())
print(t.poptop())
print(t.poptop())
print(t.poptop())
print(t.poptop())
print(t.poptop())