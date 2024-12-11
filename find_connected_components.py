def dfs(matrix, start, visited, component):
    visited[start] = True
    component.append(start)
    n = len(matrix)
    for neighbor in range(n):
        if matrix[start][neighbor] == 1 and not visited[neighbor]:
            dfs(matrix, neighbor, visited, component)

def find_connected_components(matrix):
    n = len(matrix)
    components = []
    visited = [False] * n
    
    for vertex in range(n):
        if not visited[vertex]:
            component = []
            dfs(matrix, vertex, visited, component)
            components.append(component)
    
    return components

# Пример использования
matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

components = find_connected_components(matrix)
print(components)