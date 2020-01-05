# Priority Queue Implementation using unsorted list

class PriorityQueue(object): 
    def __init__(self): 
        self.q = [] 
  
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return (len(self.q) == 0)
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.q.append(data)
  
    # for popping an element based on Priority 
    def delete(self): 
        pelement = max(self.q)
        self.q.remove(pelement)
        return pelement
  
if __name__ == '__main__': 
    myQueue = PriorityQueue() 
    myQueue.insert(12) 
    myQueue.insert(1) 
    myQueue.insert(14) 
    myQueue.insert(7) 
    print(myQueue)             
    while not myQueue.isEmpty(): 
        print(myQueue.delete())  



    
