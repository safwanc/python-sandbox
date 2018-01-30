def get_all_permutations(array):
    if len(array) <= 1: return set((array[0],))

    all_items_except_last = array[:-1]
    last_item = array[-1]

    all_permutations = get_all_permutations(all_items_except_last)
    
    permutations = set()
    for permutation in all_permutations:
        for i in range(len(permutation) + 1):
            permutations.add(permutation[:i] + [last_item] + permutation[i:])
    return permutations

words = ['ball', 'area', 'lead', 'lady']

for permutation in get_all_permutations(words):
    print(permutation)

import itertools
perms = list(itertools.permutations(words))
print(len(perms))

    