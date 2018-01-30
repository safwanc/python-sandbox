def permutations_recursive(string, result=[], l=0, r=None):
    if type(string) is str:
        string = list(string)

    if not r:  
        r = len(string) - 1

    if l == r: 
        result.append(''.join(string))
    else:
        for i in range(l, r + 1):
            string[i], string[l] = string[l], string[i]
            permutations_recursive(string, result, l + 1, r)
            string[i], string[l] = string[l], string[i]
    return result


def permutations_iterative(string):
    if type(string) is str:
        string = list(string)
    
    permutations = [[]]
    
    for char in string:
        new_permutations = list()
        for permutation in permutations:
            for i in range(len(permutation) + 1):
                new_permutations.append(permutation[:i] + [char] + permutation[i:])
                if i < len(permutation) and permutation[i] == char: 
                    break
        permutations = new_permutations

    return [''.join(permutation) for permutation in permutations]


print(permutations_recursive('SAF'))
print(permutations_iterative('SAA'))