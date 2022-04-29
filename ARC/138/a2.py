from bisect import bisect_left
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
inf = 9999999999999999999999

b = a[:k]
c = a[k:]
ans = inf

for i in range(n - k - 1):
    c[i + 1] = max(c[i + 1], c[i])

for i, a in enumerate(b):
    l = bisect_left(c, a + 1)
    if l != len(c):
        ans = min(ans, l + k - i)

print(ans if ans != inf else -1)