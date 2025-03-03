#BFS to find the shortest path
#Steps to find the shortest path with BFS
#1. Use dictionary(parent) to store each node's parent
## If we reach a node from A to B, store parent[B] = A
#2. Once we reach the destination(F), reconstruct the path by backtracking
#3. REturn the path in the correct order (from start to end)

from collections import deque

def bfs_shortest_path(graph, start, target):
    visited = set()
    queue = deque([start])
    parent = {start: None} #track where each node came from
    visited.add(start) #Add this line to mark start as visited

    while queue:
        current = queue.popleft()

        if current == target: #found the target
            #reconstruct path
            path = []
            while current is not None: #backtract path from target to start
                path.append(current)
                current = parent[current]
            return path[::-1] #reverse path from start to target
        #Explore neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current #store the parent
    return None #no path found

#Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    #find path from A to F
    path = bfs_shortest_path(graph, 'A', 'F')
    if path:
        print("Shortest path:", ' -> '.join(path))
    else:
        print("no path found")