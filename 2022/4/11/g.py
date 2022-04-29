n, k = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    if (k - friends[i][0] + 1) >= 0:
        k = (k - n) + friends[i][1]
        ans += friends[i][0]
    else:
        ans += k
        print(ans)