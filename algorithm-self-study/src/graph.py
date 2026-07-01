from collections import deque


def dfs_order(graph, start):
    visited = set()
    result = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor)

    dfs(start)
    return result


def bfs_order(graph, start):
    visited = {start}
    result = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def shortest_path_length(graph, start, target):
    if start == target:
        return 0

    visited = {start}
    queue = deque([(start, 0)])

    while queue:
        node, distance = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor == target:
                return distance + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1
