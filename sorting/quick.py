'''
Quick Sort
Runtime: O(n log(n)) & Space: O(log(n))
'''

def partition(array, left, right):
    pivot = array[(left + right) // 2]
    while left <= right:
        while array[left] < pivot: left += 1
        while array[right] > pivot: right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left, right = left + 1, right - 1
    return left

def quick_sort(array, left=0, right=None):
    if right is None: right = len(array) - 1
    if left >= right: return
    pivot = partition(array, left, right)
    quick_sort(array, left, pivot - 1)
    quick_sort(array, pivot, right)
    print(array)

from numpy.random import randint
quick_sort(randint(100, size=25).tolist())