h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]


flg = True
for i in range(h - 1):
    for j in range(i + 1, h):
        #print(i, j)
        for k in range(w - 1):
            for l in range(k + 1, w):
                #print(k, l)
                #print(a[i][k] + a[j][l], a[j][k] + a[i][l])
                if a[i][k] + a[j][l] > a[j][k] + a[i][l]:
                    flg = False
                    break
if flg:
    print("Yes")
else:
    print("No")