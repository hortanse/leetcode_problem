#Dijkstra's algorithm for shortest path in a weighted graph
#1. Use a priority queue to always expand the smallest distance node
#2. Initialize distances with infinity and the start node with 0
#3. Process nodes from the priority queue until it's empty
#4. For each node, update the distances of its neighbors and add them to the queue
#5. Return the distances dictionary containing the shortest distances to all nodes
import heapq

def dijkstra(graph, start):
    #Step 1: Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    #Step 2: Process nodes from the priority queue
    priority_queue = [(0, start)] # source node with 0 distance
   
    while priority_queue:
        #Step 3: Pop the smallest distance node from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue) #pop smallest distance node
        #Step 4. Process all neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight #calculate distance to neighbor
            #step 5. If shorter distance is found, update distance and add to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor)) #push updated distance and neighbor to priority queue

    return distances #return the shortest distances to all nodes

#Example usage
if __name__ == "__main__":
    graph = {
        'A': [('B', 4), ('C', 1)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
print(dijkstra(graph, 'A'))
