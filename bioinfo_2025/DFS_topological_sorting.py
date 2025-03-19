#DFS topological sorting
#1. Use a visited set to track processed nodes
#2. Use a stack to store the topological order
#3. Perform DFS, adding nodes to stack after processing their nieghbors
#4. Reserve the stack to get the correct order

def topological_sort_dfs(graph):
    visited = set()
    result = [] # initialize empty list to store topological order

    def dfs(node): #helper function to perform DFS
        if node in visited:
            return
        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor) #recurse on unvisited neighbors
        result.append(node) #add node to result after processing all neighbors
    #Run DFS on all nodes (to handle disconnected components)
    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1] #reverse result to get correct order

#Example usage
if __name__ == "__main__":
    graph = {
        'A': ['C'],
        'B': ['D'],
        'C': ['D'],
        'D': []
    }
    print(topological_sort_dfs(graph))