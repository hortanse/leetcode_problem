#Breadth-first search BFS in graph
#BFS explores all neighbors before going deeper
#Use a queue(FIFO) instead of a stack
#great for finding shortest paths in graphs

from collections import deque

def bfs(graph, start):
    visited = set() #keep track of visited nodes
    queue =  deque([start]) #Initialize queue with start node
    visited.add(start) #mark start node as visited

    while queue: # While there are nodes to process
        vertex = queue.popleft() #get the next node
        print(vertex, end=" ") #print node and process it

        #Add unvisited neighbors to queue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#Example usage
if __name__ == "__main__":
    # Example graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print("BFS starting from vertex 'A':")
    bfs(graph, 'A')