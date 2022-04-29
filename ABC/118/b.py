n, m = map(int, input().split())
k = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(1, m+1):
    flag = True
    for j in range(n):
        if i not in k[j][1:]:
            flag = False
            break
    if flag:
        ans += 1
print(ans)