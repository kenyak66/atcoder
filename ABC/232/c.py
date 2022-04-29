n, m = map(int, input().split())
g1 = [[] for i in range(m)]
g1len = [] 
for i in range(m):
    a, b = map(int, input().split())
    g1[a - 1].append(b)
    g1[b - 1].append(a)
for i in g1:
    g1len.append(len(i))
g1len.sort()

g2 = [[] for i in range(m)]
g2len = []
for i in range(m):
    a, b = map(int, input().split())
    g2[a - 1].append(b)
    g2[b - 1].append(a)
for i in g2:
    g2len.append(len(i))
g2len.sort()

if g1len == g2len:
    print("Yes")
else:
    print("No")