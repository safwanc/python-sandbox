'''
Radix Sort
Runtime: O(kn) Space: O(n)
'''

def radix_sort(array):
    buckets = [list() for _ in range(10)]
    max_value = max(array)
    divisor = 1

    while max_value > divisor:
        for num in array:
            buckets[(num // divisor) % 10].append(num)
        print('Bucketed by {}s:'.format(divisor), buckets)

        array = list()
        for i in range(10):
            array.extend(buckets[i])
            buckets[i] = list()
        print('Sorted by {}s'.format(divisor), array, '\n')

        divisor *= 10

    return array



from numpy.random import randint
n = 10000000
radix_sort(randint(n, size=25).tolist())