from collections import defaultdict
class graph:
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
    def add_edge(self, start, end):
        self.graph[start].append(end)

    def dfs(self): 
        ver_count = len(self.graph)  #total vertices 
        # Mark all the vertices as not visited 
        visited =[False]*(ver_count) 
  
        # Call the recursive helper function to print 
        # DFS traversal starting from all vertices one 
        # by one 
        for i in range(ver_count):
            if visited[i] == False: 
                self.dfs_util(i, visited) 

    def dfs_util(self, v, visited):
        visited[v]= True
        print (v, end = " ") 
        # Recur for all the vertices adjacent to 
        # this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.dfs_util(i, visited) 

    def bfs(self, s=0):
        ver_count = len(self.graph)  #total vertices 
        # Mark all the vertices as not visited 
        visited = [False] * (ver_count) 
        # Create a queue for BFS 
        queue = []
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s)
        visited[s] = True
        while queue: 
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i)
                    visited[i] = True


g = graph() 
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
  
print("Following is Depth First Traversal")
g.dfs()
#g.bfs()