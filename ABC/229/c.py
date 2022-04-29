n, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]

c.sort()
c2 = c[::-1]

ans = 0
cnt = 0
for i in range(n):
    if cnt + c2[i][1] <= w:
        cnt += c2[i][1]
        ans += c2[i][0] * c2[i][1]
    else:
        while cnt < w:
            cnt += 1
            ans += c2[i][0]
        break
print(ans)