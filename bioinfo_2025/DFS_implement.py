#Depth-First search
#Implement DFS (Recursion)
def dfs_recursive(graph, node, visited=None):
    # Initialize visited set on first call
    if visited is None:
        visited = set()
    
    # Mark current node as visited
    visited.add(node)
    print(node, end=' ')
    
    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

#Implement DFS (Iterative)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            stack.extend(graph[node][::-1]) #reverse the order of neighbors to match recursive DFS

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    
    print("DFS traversal:")
    dfs_recursive(graph, 'A')
    print("\nDFS traversal (Iterative):")
    dfs_iterative(graph, 'A')