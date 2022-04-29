n = int(input())
inf = 998244353

dp = [[0] * 9 for _ in range(n)]
dp[0] = [1]*9

for i in range(1, n):
    for j in range(9):
        dp[i][j] += dp[i-1][j]
        if j >= 1:
            dp[i][j] += dp[i-1][j-1]
        if j <= 7:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= inf

print(sum(dp[n-1]) % inf)