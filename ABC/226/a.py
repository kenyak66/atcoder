x = float(input())

ans = int((x*1000) // 100)
if ans % 10 < 5:
    print(ans // 10)
else:
    print(ans // 10 + 1)