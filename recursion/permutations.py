array = [1, 2, 3, 1]

def get_all_permutations(array):
    if len(array) <= 1:
        return [array]

    all_except_last, last = array[:-1], array[-1]

    result = list()
    perms = get_all_permutations(all_except_last)
    for perm in perms:
        for i in range(len(all_except_last) + 1):
            result.append(perm[:i] + [last] + perm[i:])
    return result

def iterative_permutations(array):
    perms = [[]]

    for num in array:
        new = list()
        for perm in perms:
            for i in range(len(perm) + 1):
                new.append(perm[:i] + [num] + perm[i:])
        perms = new
        print(perms)

    return perms


perms = get_all_permutations(array)
print(len(perms), perms)

perms = iterative_permutations(array)
print(len(perms), perms)

import itertools
perms = list(itertools.permutations(array))
print(len(perms), perms)
