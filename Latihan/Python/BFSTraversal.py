from collections import deque

class BFSTraversal:
    def __init__(self, data):
        self.node = data
        self.adj = [[] for i in range(data)]
        self.queue = deque()

    def insertEdge(self, i, j):
        self.adj[i].append(j)

    def BFS(self, i):
        nodes = [False] * self.node
        nodes[i] = True
        self.queue.append(i)
        while self.queue:
            i = self.queue.popleft()
            print(i, end=' ')
            for j in self.adj[i]:
                if not nodes[j]:
                    nodes[j] = True
                    self.queue.append(j)


graph = BFSTraversal(6)
graph.insertEdge(0, 1)
graph.insertEdge(0, 3)
graph.insertEdge(0, 4)
graph.insertEdge(4, 5)
graph.insertEdge(3, 5)
graph.insertEdge(1, 2)
graph.insertEdge(1, 0)
graph.insertEdge(2, 1)
graph.insertEdge(4, 1)
graph.insertEdge(3, 1)
graph.insertEdge(5, 4)
graph.insertEdge(5, 3)
print("Breadth First Traversal for the graph is: ")
graph.BFS(0)