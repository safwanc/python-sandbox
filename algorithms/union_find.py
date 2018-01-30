


def find(x):
    return x if parents[x] == x else find(parents[x])

def union(edge):
    x, y = [find(n) for n in edge]
    parents[y] = x
    print(parents)
    return x != y

def is_valid_tree(n, edges):
    return len(edges) == n - 1 and all(union(edge) for edge in edges)

parents = list(range(5))
print(is_valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))

parents = list(range(5))
print(is_valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

