##Program to implement MAX heap
# So a few things to remember is that when percollating downwards, we have to compare against both left and right, while
# on percollating upwards we only have to compare against the node, hence adding new element is slightly simpler, cause we 
# need not check between two children.


class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.size = 0


    def percup(self,i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i],self.heapList[i//2] = self.heapList[i//2],self.heapList[i]
            i = i//2


    def insert(self,val):
        self.heapList.append(val)
        self.size + =1
        self.percup(self.size)


    def minchild(self,i):
        if (i*2) + 1 > self.size:
            return i * 2
        if self.heapList[i*2] > self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1


    def percdown(self,i=1):
        while (i * 2) <= self.size:
            ci = self.minchild(i)
            if self.heapList[i] < self.heapList[ci]:
                self.heapList[i], self.heapList[ci] = self.heapList[ci], self.heapList[i]
            i = ci


    def delete(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size - = 1
        self.heapList.pop()
        self.percdown()
        return retval