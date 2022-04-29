n, k, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
can = 0

for i in range(n):
    can += a[i]//x
    a[i] = a[i]%x

a.sort(reverse=True)

if can >= k:
    ans = sum(a) + can*x - k*x
else:
    if k < can + n:
        for i in range(k - can):
            a[i] = 0
        ans = sum(a)

print(ans)