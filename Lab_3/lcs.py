def lcs_length(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[m][n]

s1 = "Kundana"
s2 = "danny"

length = lcs_length(s1, s2)
print(length)