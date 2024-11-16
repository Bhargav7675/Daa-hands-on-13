from collections import defaultdict

# Graph class representing a directed graph
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    # Add edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # Helper function to perform topological sort
    def topological_sort_util(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        
        # Recur for all adjacent vertices
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        # Push current vertex to the stack
        stack.insert(0, v)
    
    # Function to perform topological sort
    def topological_sort(self):
        visited = {key: False for key in self.graph}
        stack = []
        
        # Call the recursive helper function for each vertex
        for vertex in self.graph:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)
        
        return stack
3