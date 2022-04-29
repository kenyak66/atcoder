n = int(input())
a = list(map(int, input().split()))

dp = [0][0] * (n + 1)
ans = [0] * n
ans2 = [0] * n
for i in range(1, n + 1):
    dp1 = dp[i - 1]
    dp2 = (dp[i - 2] * a[i - 2]) / a[i - 1]
    dp3 = (dp[i - 3] * a[i - 3]) / a[i - 1]
    if i == 1:
        dp[1] = 1
    elif i == 2:
        if dp1 >= dp2:
            dp[i] = dp1
            ans[i - 1] = 0
        if dp1 < dp2:
            dp[i] = dp2
            ans[i - 2], ans[i - 1] = 1, 1
    else:
        if dp1 == max(dp1, dp2, dp3):
            dp[i] = dp1
            ans[i - 1] = 0
        if dp2 == max(dp1, dp2, dp3):
            dp[i] = dp2
            ans[i - 2], ans[i - 1] = 1, 1
        if dp3 == max(dp1, dp2, dp3):
            dp[i] = dp3
            ans[i - 3], ans[i - 2], ans[i - 1] = 1, 0, 1

print(*ans)
print(dp[n])