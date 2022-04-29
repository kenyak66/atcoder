n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]

A = sum(a)
r = 0
l = 0
rcnt = 0
lcnt = 0
rnext = 0
lnext = 0

while r + l < A:
    l += (b[n - 1 - lcnt]) / 60
    if l >= lnext + a[n - 1 - lcnt]:
        lcnt += 1
        lnext += a[n - 1 - lcnt]

    r += (b[rcnt]) / 60
    if r >= rnext + a[rcnt]:
        rcnt += 1
        rnext += a[rcnt]

print(r)
