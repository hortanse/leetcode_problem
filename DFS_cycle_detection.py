#Cycle detection in a directed graph using DFS
#key idea: 1. Use recursion_stack to de
# 2. Use DFS with a parent variable for und
#2. IF we encounter a visited node that is NOT the parent, then there is a cycle

def dfs_cycle_directed(graph, node, visited, recursion_stack):
    visited.add(node) #mark current node as visited
    recursion_stack.add(node) #add to recursion stack to track nodes in current path

    for neighbor in graph[node]:
        if neighbor not in visited: #Visit unv
            if dfs_cycle_directed(graph, neighbor, visited, recursion_stack): #recurse on unvisited neighbor
                return True #cycle detected
        elif neighbor in recursion_stack: #check if neighbor is in recursion stack
            return True #cycle detected
    recursion_stack.remove(node) #remove node before backtracking
    return False #no cycle detected

def dfs_cycle_undirected(graph, node, visited, parent):
    visited.add(node) #mark current node as visited
    for neighbor in graph[node]:
        if neighbor not in visited: #visit unvisited neighbor
            if dfs_cycle_undirected(graph, neighbor, visited, node): #recurse on unvisited neighbor
                return True #cycle detected if a cycle is found
        elif neighbor != parent: #check if neighbor is not the parent
            return True #cycle detected
    return False #no cycle detected

#Example usage
if __name__ == "__main__":
    graph_undirected = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E'] #Cycle exists (F -> E -> B -> F)
    }
    graph_directed = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['E'],
        'E': ['B'] #Cycle exists (B -> C -> D -> E -> B)
    }
    print(dfs_cycle_directed(graph_directed, 'A', set(), set()))
    print(dfs_cycle_undirected(graph_undirected, 'A', set(), None))
