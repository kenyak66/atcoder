n = int(input())
v = list(map(int, input().split()))

v.sort()
for i in range(n-1):
    av = (v[0] + v[1])/2
    v.remove(v[0])
    v.remove(v[0])
    v = [av] + v
print(v[0])