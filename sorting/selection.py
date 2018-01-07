'''
Selection Sort
Runtime: O(n^2) & Space: O(1)
'''

import operator
def selection_sort(array):
    array_slice_from = lambda start_index: ((i, array[i]) for i in range(start_index, len(array)))
    for index, value in enumerate(array):
        min_index, min_value = min(array_slice_from(index), key=operator.itemgetter(1))
        array[index], array[min_index] = array[min_index], array[index]
        print('Pass {}: {}'.format(index + 1, array))

from numpy.random import randint
selection_sort(randint(100, size=25).tolist())