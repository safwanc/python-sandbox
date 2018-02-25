s1 = 'sunday'
s2 = 'saturday'

def brute_force(s1, s2, m=len(s1), n=len(s2)):
    if m == 0: return n
    if n == 0: return m
    
    if s1[m-1] == s2[n-1]:
        return brute_force(s1, s2, m-1, n-1)
    
    return 1 + min(
        brute_force(s1, s2, m, n-1),
        brute_force(s1, s2, m-1, n),
        brute_force(s1, s2, m-1, n-1)
    )

def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0: dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    return dp[m][n]

print(brute_force(s1, s2))
print(edit_distance(s1, s2))