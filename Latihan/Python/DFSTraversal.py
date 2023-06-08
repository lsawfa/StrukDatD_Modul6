from collections import defaultdict

class DFSTraversal:
    def __init__(self, v):
        self.adj = defaultdict(list)
        self.visited = [False] * v

    def insertEdge(self, src, dest):
        self.adj[src].append(dest)

    def DFS(self, vertex):
        self.visited[vertex] = True
        print(vertex, end=' ')
        for n in self.adj[vertex]:
            if not self.visited[n]:
                self.DFS(n)

graph = DFSTraversal(8)
graph.insertEdge(0, 1)
graph.insertEdge(0, 2)
graph.insertEdge(0, 3)
graph.insertEdge(1, 3)
graph.insertEdge(2, 4)
graph.insertEdge(3, 5)
graph.insertEdge(3, 6)
graph.insertEdge(4, 7)
graph.insertEdge(4, 5)
graph.insertEdge(2, 2)
print("Depth First Traversal for the graph is: ")
graph.DFS(0)