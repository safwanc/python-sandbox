from collections import defaultdict
import heapq

edges = [
    ('A', 'D', 1),
    ('A', 'B', 3),
    ('B', 'D', 3),
    ('B', 'C', 1),
    ('D', 'C', 1),
    ('D', 'E', 6),
    ('C', 'F', 4),
    ('C', 'E', 5),
    ('E', 'F', 2),
]

def prims_mst(edges, start):
    mst, visited, heap = list(), set(), [(0, start, (start,))]
    graph = defaultdict(list)

    for f, t, c in edges:
        graph[f].append((t, c))
        graph[t].append((f, c))

    while heap:
        weight, node, edge = heapq.heappop(heap)
        if node not in visited:
            mst.append(edge + (weight,))
            visited.add(node)
            for t, c in graph[node]:
                if t not in visited:
                    heapq.heappush(heap, (c, t, (node, t)))
    return mst


print(prims_mst(edges, 'A'))