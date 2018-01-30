A = [4, 3, 2, 6]
n = len(A)

B = [A[k:] + A[:k] for k in range(n)]

print(B)

for i in range(10):
    pass

print(i)