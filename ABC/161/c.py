n, k = map(int, input().split())

ans = n
if ans >= k:
    ans = ans%k
if ans < k:
    ans = min(ans, abs(ans - k))

print(ans)