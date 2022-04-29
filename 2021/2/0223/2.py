import bisect

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = list(int(input()) for _ in range(q))

a.sort()

for i in range(q):
    l = bisect.bisect_left(a, b[i])

    if l == 0:
        print(abs(a[l]-b[i]))
    elif l == n:
        print(abs(a[l-1]-b[i]))
    else:
        print(min(abs(a[l]-b[i]), abs(a[l-1]-b[i])))
    
    