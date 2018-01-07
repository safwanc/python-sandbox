'''
Merge Sort
Runtime: O(n log(n)) & Space: O(n) ..if not slicing all the way to hell
'''

def merge_sort(array):
    if len(array) > 1:
        print('Split', array)
        midpoint = len(array) // 2
        left, right = array[:midpoint], array[midpoint:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                array[k], i, k = left[i], i + 1, k + 1
            else: 
                array[k], j, k = right[j], j + 1, k + 1
        
        while i < len(left):
            array[k], i, k = left[i], i + 1, k + 1
        
        while j < len(right):
            array[k], j, k = right[j], j + 1, k + 1

    print('Merging', array)


from numpy.random import randint
merge_sort(randint(100, size=25).tolist())