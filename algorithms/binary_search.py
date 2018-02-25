def binary_search_recursive(target, numbers):
    if len(numbers) == 0 or target < numbers[0] or target > numbers[-1]:
        return False

    middle_index = len(numbers) // 2
    middle_value = numbers[middle_index]

    if target < middle_value:
        return binary_search_recursive(target, numbers[:middle_index])
    elif target > middle_value:
        return binary_search_recursive(target, numbers[middle_index:])
    else:  # middle_value == target
        return True

def binary_search_iterative(target, numbers):
    l, h = 0, len(numbers) - 1
    while l <= h:
        m = (l + h) // 2
        if numbers[m] < target: l = m + 1
        elif numbers[m] > target: h = m - 1
        else: return True
    
    return False


test_cases = {
    1: [],
    2: [2],
    9: [1, 2],
    3: [1, 2, 3, 4, 5]
}

for approach in [binary_search_recursive, binary_search_iterative]:
    print('Using approach', str(approach))
    for target, numbers in test_cases.items():
        print('{} in {}? -> {}'.format(target, numbers, binary_search_iterative(target, numbers)))
    print('--')