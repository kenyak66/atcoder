n = int(input())
h = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    if h[i] <= h[i-1]:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = 0
print(max(dp))