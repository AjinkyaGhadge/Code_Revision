#Program to test the python heapq module

import heapq
l = [10,4,6,3,7]
print("The list is ", end="")
print(l)
heapq.heapify(l)
print("The heap is ", end="")
print(l)
print(heapq.heappop(l))
print(heapq.heappop(l))
print(heapq.heappop(l))