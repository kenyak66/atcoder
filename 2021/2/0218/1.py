h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

b = []
c = []
ans = [[]for _ in range(h)]

for i in a:
    b.append(sum(i))

for i in range(w):
    W = 0
    for j in range(h):
        W += a[j][i]
    c.append(W)

for i in range(h):
    for j in range(w):
        ans[i].append(b[i] + c[j] - a[i][j])

# print(b)
# print(c)
for i in ans:
    print(*i)