def dfs(graph, visited, node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, visited, neighbor)
def is_connected(graph):
    visited = set()
    start_node = list(graph.keys())[0]
    dfs(graph, visited, start_node)
    return len(visited) == len(graph)
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}
if is_connected(graph):
    print("Graph is connected")
else:
    print("Graph is not connected")