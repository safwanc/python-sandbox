'''
A sorted array is rotated at some point, find that point via binary search
'''

import random

A = list(range(100))
n = random.randint(0, len(A) - 1)
A = A[n:] + A[:n]

def find_pivot(A):
    left, right = 0, len(A) - 1
    while left < right:
        midpoint = left + (right - left) // 2
        if A[midpoint] > A[right]:
            left = midpoint + 1
        else:
            right = midpoint
    return left

pivot = find_pivot(A)
print('Rotated', A)
print('A[{i}] = {j}'.format(i=pivot, j=A[pivot]))
print('Unrotated', A[pivot:] + A[:pivot])
