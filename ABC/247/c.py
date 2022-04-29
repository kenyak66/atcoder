n = int(input())

dp = ['0']*n
print(dp)
dp[0] = '1'

for i in range(1, n):
    dp[i] = dp[i-1] + ' ' + str(i+1) + ' ' + dp[i-1]
print(dp[n-1])