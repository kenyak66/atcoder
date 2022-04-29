from bisect import bisect_left

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
start = bisect_left(a, x)

if start < m/2:
    b = a[:start]
else:
    b = a[start:]

print(len(b))