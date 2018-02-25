from collections import defaultdict
import operator
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

def kruskals_mst(edges):
    mst, parents = list(), defaultdict(lambda: -1)

    find = lambda u: u if parents[u] == -1 else find(parents[u])
    edges.sort(key=operator.itemgetter(2))

    for f, t, c in edges:
        if find(f) == find(t): continue
        mst.append((f, t, c))
        parents[find(f)] = find(t)
    return mst

print(kruskals_mst(edges))