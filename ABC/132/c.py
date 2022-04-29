n = int(input())
d = list(map(int, input().split()))

d.sort()
l, r = n//2-1, n//2
print(d[r]- d[l])