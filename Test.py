# Test case for Topological Sort
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Expected output: A valid topological sort (e.g., [5, 4, 2, 3, 1, 0])
print("Topological Sort:", g.topological_sort())

# Test case for Depth-First Search
graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [5],
    5: []
}

# Expected output: A valid DFS traversal (e.g., [1, 3, 2, 4, 5])
print("DFS:", dfs(graph, 1))

# Test case for Kruskal's Algorithm
vertices = [0, 1, 2, 3, 4]
wg = WeightedGraph(vertices)
wg.add_edge(0, 1, 10)
wg.add_edge(0, 2, 6)
wg.add_edge(0, 3, 5)
wg.add_edge(1, 3, 15)
wg.add_edge(2, 3, 4)

# Expected output: A valid Minimum Spanning Tree
mst = wg.kruskal()
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"({edge.src} - {edge.dest}): {edge.weight}")