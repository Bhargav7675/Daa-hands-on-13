# Helper class representing an edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Disjoint Set (Union-Find) class
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    # Find the root of a set
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    # Union two sets
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_v] < self.rank[root_u]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Graph class representing a connected, undirected graph with weighted edges
class WeightedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    
    # Add an edge to the graph
    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))
    
    # Function to find the MST using Kruskal's algorithm
    def kruskal(self):
        # Sort edges by weight
        self.edges.sort(key=lambda e: e.weight)
        
        # Initialize Disjoint Set
        disjoint_set = DisjointSet(self.vertices)
        
        mst = []
        
        # Iterate through the sorted edges
        for edge in self.edges:
            # Check if adding this edge forms a cycle
            if disjoint_set.find(edge.src) != disjoint_set.find(edge.dest):
                mst.append(edge)
                disjoint_set.union(edge.src, edge.dest)
        
        return mst
