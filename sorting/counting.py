'''
Counting Sort
Runtime: O(n) Space: O(n) ..if the range of n is known
'''

def counting_sort(array, max_value):    
    buckets = [array.count(n) for n in range(max_value + 1)]
    result = [n for n, count in enumerate(buckets) for _ in range(count)]
    print('Unsorted', array)
    print('Buckets', list(enumerate(buckets)))
    print('Sorted', result)
    return result

from numpy.random import randint
n = 100
counting_sort(randint(n, size=25).tolist(), n)