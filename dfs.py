def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))
    return visited

# Exemple d'utilisation
if __name__ == "__main__":
    graph = {
        1: [3],
        2: [4],
        3: [1],
        4: [2]
    }
    print(dfs(graph, 1))  # Résultat: [1, 3]
def dfs_path_length(graph, start, end):
    visited = []
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop()
        if node == end:
            return depth
        if node not in visited:
            visited.append(node)
            for neighbor in reversed(graph[node]):
                stack.append((neighbor, depth + 1))
    return -1  # Si aucun chemin trouvé
#Add points
