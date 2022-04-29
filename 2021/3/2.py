n, k = map(int, input().split())
h = list(map(int, input().split()))

# Pythonのintに最大値は無し！！
dp = [10**100]*n
dp[0] = 0
dp[1] = abs(h[0] - h[1])
for i in range(2, n):
    for j in range(1, min(k, i) + 1):
        # print(dp[i], dp[i-j] + abs(h[i] - h[i-j]))
        dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))
# print(dp)
print(dp[-1])