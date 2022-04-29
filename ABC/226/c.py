n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

ans = t[n - 1][0]
for i in range(t[n - 1][1]):
    waza = t[n - 1][1 + 2]
    while waza 