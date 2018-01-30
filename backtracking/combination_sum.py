candidates = [2, 3, 6, 7]
target = 7
results = list()

def combo_sum(candidates, target, i=0, solution=list()):
    if target < 0:
        print('Discarding', solution)
        return
    elif target == 0:
        print('Keeping', solution)
        results.append(solution[:])

    for j in range(i, len(candidates)):
        candidate = candidates[j]
        solution.append(candidate)
        combo_sum(candidates, target - candidate, j, solution)
        solution.pop()

combo_sum(candidates, target)
print(results)