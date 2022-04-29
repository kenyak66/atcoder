n, m = map(int, input().split())
id = [list(map(int, input().split())) for _ in range(m)]

x = 0
y = n
for i in range(m):
    if id[i][0] > x:
        x = id[i][0]
    if id[i][1] < y:
        y = id[i][1]

print(y - x + 1)