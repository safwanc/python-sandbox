
from collections import defaultdict
import heapq

edges = [
    ('A', 'B', 7),
    ('A', 'D', 5),
    ('B', 'C', 8),
    ('B', 'D', 9),
    ('B', 'E', 7),
    ('C', 'E', 5),
    ('D', 'E', 15),
    ('D', 'F', 6),
    ('E', 'F', 8),
    ('E', 'G', 9),
    ('F', 'G', 11)
]

def dijkstras(edges, node):
    graph = defaultdict(list)
    for f, t, c in edges: graph[f].append((t, c))
    heap, visited = [(0, node)], set()
    shortest = defaultdict(lambda: float('inf'))

    while heap:
        cost, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            shortest[node] = cost
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor))
    
    return shortest
    


print(dijkstras(edges, 'A'))