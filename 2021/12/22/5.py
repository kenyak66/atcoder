n, x = map(int, input().split())
vp = list(list(map(int, input().split())) for _ in range(n))

flg = True
alk = 0
for i in range(n):
    alk += vp[i][0]*vp[i][1]

    if alk > x*100:
        flg = False
        print(i+1)
        break

if flg == True:
    print(-1)