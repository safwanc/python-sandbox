'''
Bubble Sort
Runtime: O(n^2) & Space: O(1)
'''

def bubble_sort(array):
    iteration, done = 0, False
    while not done:
        iteration, done = iteration + 1, True
        print('Pass {}: {}'.format(iteration, array))
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i], array[i-1] = array[i-1], array[i]
                done = False

from numpy.random import randint
bubble_sort(randint(100, size=25).tolist())