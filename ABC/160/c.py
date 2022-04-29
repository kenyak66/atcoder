k, n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = []
for i in range(n):
    if i != n-1:
        b.append(a[i+1] - a[i])
    else:
        b.append(k - (a[i] - a[0]))

print(sum(b) - max(b))