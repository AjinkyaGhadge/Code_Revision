# Program to Implement Adjacency List, DFS and BFS in Graph

import collections
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connected To ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    

class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def addVertex(self,key):
        self.numVertices = self.numVertices+1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self,n):
        return n in self.vertList
    
    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],weight)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

    def dfs(self,start,visited = None):
        if visited == None:
            visited = set()
        visited.add(start)
        vert = self.getVertex(start)
        tempset = vert.getConnections()
        l = set()
        for i in tempset:
            l.add(i.getId())
        for nex in l-visited:
            self.dfs(nex,visited)
        return visited
    
    def bfs(self,start):
        q = collections.deque()
        q.append(start)
        visited = set()
        k = list()
        while(q):
            x = q.popleft()
            k.append(x)
            visited.add(x)
            vert = self.getVertex(x)
            tempset = vert.getConnections()
            for i in tempset:
                if i.getId() not in visited:
                    q.append(i.getId())
        return(k)





g = Graph()
for i in range(6):
    g.addVertex(i)
g.vertList
g.addEdge(0,1,5)
g.addEdge(0,7,2)
g.addEdge(1,2,2)
g.addEdge(1,9,2)
g.addEdge(2,3,4)
g.addEdge(3,5,9)
g.addEdge(5,0,7)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

print(g.dfs(0))
print(g.bfs(0))
