graph = {
    0: set([0, 1]),
    1: set([0, 1]),
    2: set([]),
    3: set([4, 3]),
    4: set([3, 4]),
}

disjoint_sets = list()

for node, neighbours in graph.items():
    mergeable_set_found = False
    for s in disjoint_sets:
        if neighbours & s:
            s.update(neighbours)
            mergeable_set_found = True
            break
    
    if not mergeable_set_found:
        disjoint_sets.append(neighbours)

    

print(disjoint_sets)