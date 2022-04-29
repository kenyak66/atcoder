h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

ans = [[]for _ in range(w)]

for i in range(h):
    for j in range(w):
        ans[j].append(a[i][j])

for i in range(w):
    print(*ans[i])