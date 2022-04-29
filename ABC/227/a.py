n, k, a  = map(int, input().split())
cnt = k - (n - (a - 1))
if cnt >= 0:
    ans = (k - (n - (a - 1))) % n
    print(ans if ans != 0 else n)
else:
    print((a - 1) + k)