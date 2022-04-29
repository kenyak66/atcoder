n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * n
num = []
for i in range(n):
    dp[i] = t[i][0]
    for j in range(t[i][1]):
        waza = t[i][j + 2] - 1
        if waza :
            num.append(waza)
            dp[i] += dp[waza]
        else:
            dp[i] += t[waza][0]

print(dp[n - 1])