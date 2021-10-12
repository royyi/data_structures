# Roy Yi
# 9/21/21
# Build adjacency list graph data structure

from collections import defaultdict
  
class Graph:
    # represent graph using dictionary of lists
    def __init__(self):
        self.graph = defaultdict(list)
  
    def add_edge(self, u, v):
        self.graph[u].append(v)
  
    def dfs_helper(self, u, visited):
        visited.add(u)
        print(u)
  
        for v in self.graph[u]:
            if v not in visited:
                self.dfs_helper(v, visited)
  
    def dfs(self, u):
        visited = set()
        self.dfs_helper(u, visited)

def main():
    g = Graph()

    for e in [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]:
        g.add_edge(*e)

    g.dfs(2)

if __name__ == "__main__":
    main()
