'''
Longest Continuous Subsequence
'''

s1 = 'ABCDGH'
s2 = 'AEDFHR'

def print2d(array):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in array]))

def brute_force(s1, s2, i=len(s1), j=len(s2)):
    if i == 0 or j == 0: return 0
    if s1[i-1] == s2[j-1]: return 1 + brute_force(s1, s2, i-1, j-1)
    else: return max(brute_force(s1, s2, i-1, j), brute_force(s1, s2, i, j-1))


def lcs(s1, s2):
    m, n = len(s1), len(s2)
    L = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0: continue
            elif s1[i-1] == s2[j-1]: L[i][j] = 1 + L[i-1][j-1]
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
        print2d(L)
        print('\n')
    
    return L[m][n]

print(brute_force(s1, s2))
print(lcs('ABC', 'BCD'))