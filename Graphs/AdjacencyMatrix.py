# Program to Implement Adjacency Matrix

adj_mat = [[0,3,0,0,0],[0,0,2,0,0],[0,0,0,0,9],[3,0,0,0,0],[1,0,0,0,0]]

def BFS(adj_mat):
    visited = set()
    l = list()
    for i,j in enumerate(adj_mat):
        if i not in visited:
                    visited.add(i)
                    l.append(i)
        for m,n in enumerate(adj_mat[i]):
            if n!=0:
                if m not in visited:
                    visited.add(m)
                    l.append(m)

    return l

def DFS(adj_mat,start,visited=None):
    if visited == None:
        visited = set()
    if start not in visited:
        visited.add(start)
    
    for i in range(len(adj_mat[start])):
        if i not in visited:
            DFS(adj_mat,i,visited)
    return visited
    

print(BFS(adj_mat))
print(DFS(adj_mat,0))