n = int(input())
a = list(map(int, input().split()))

flg = True
for i in a:
    if i == 0:
        print(0)
        flg = False

if flg == True:
    ans = 1
    cnt = 0
    while(ans <= 1e+18):
        ans *= a[cnt]
        cnt += 1
        if cnt >= len(a):
            break

    if ans <= 1e+18:
        print(ans)
    else:
        print(-1)