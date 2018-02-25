import collections
import itertools

cost_edge_list = [
    (1, 3, 15),
    (1, 4, 20),
    (1, 2, 10),
    (3, 2, 35),
    (3, 4, 30),
    (2, 4, 25),
]

graph = collections.defaultdict(set)
costs = collections.defaultdict(int)

for f, t, c in cost_edge_list:
    graph[f].add(t)
    graph[t].add(f)
    costs[(f, t)] = c
    costs[(t, f)] = c

def brute_force():
    '''
    O(n!) runtime since we generate all possible permutations
    '''
    min_cost = float('inf')
    for perm in itertools.permutations(graph.keys()):
        paths = [tuple([perm[i], perm[(i+1)%len(perm)]]) for i in range(len(perm))]
        if not all(path in costs for path in paths): continue
        min_cost = min(min_cost, sum(costs[path] for path in paths))
    return min_cost

def subsets(array):
    subsets = [[]]
    for i in array:
        subsets.extend([subset + [i] for subset in subsets])
    return [set(subset) for subset in subsets]

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

dist = lambda i, j: cost_matrix[i][j]

def held_karp_algo():
    sets = subsets(range(1, 4))
    sets.sort(key=len)
    print(sets)

held_karp_algo()