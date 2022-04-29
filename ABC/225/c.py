n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
 
flg = True
 
if m == 1:
    for l in range(n - 1):
        if b[l + 1][0] - b[l][0] != 7:
            flg = False
            break

elif n == 1:
    for p in range(m - 1):
        if b[0][p + 1] - b[0][p] != 1:
            flg = False
            break

else:
    for k in range(m - 1):
        if b[0][k + 1] - b[0][k] != 1:
            flg = False
            break
        elif b[1][k] - b[0][k] != 7:
            flg = False
            break
 
    if flg:
        for i in range(1, n - 1):
            for j in range(m - 1):
                    if b[i + 1][j] - b[i][j] != 7:
                        flg = False
                        break
 
print("Yes" if flg else "No")