n, m = map(int, input().split())
g = [[] for _ in range(n)]
ans = [0]*n

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b)
    g[b-1].append(a)

    if a>b:
        ans[a-1] += 1
    if b>a:
        ans[b-1] += 1

print(ans.count(1))