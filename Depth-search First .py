# Function to perform DFS from a given starting vertex
def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add all adjacent vertices to the stack
            stack.extend(graph[vertex])
    
    return result
