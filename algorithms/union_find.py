


def find(x):
    return x if parents[x] == x else find(parents[x])

def union(edge):
    x, y = [find(n) for n in edge]
    parents[y] = x
    print(parents)
    return x != y

def is_valid_tree(n, edges):
    return len(edges) == n - 1 and all(union(edge) for edge in edges)

def union_find(n, edges):
    parents = {p: -1 for p in range(n)}
    
    def find(v):
        return v if parents[v] == -1 else find(parents[v])
    
    for u, v in edges:
        parent_u, parent_v = find(u), find(v)
        if parent_u == parent_v: return True
        else: parents[parent_u] = parent_v
    
    return len(edges) == n - 1

parents = list(range(5))
print(is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

parents = list(range(5))
print(is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


print(union_find(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
