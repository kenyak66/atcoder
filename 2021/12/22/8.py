a, b = map(float, input().split())

ans = a * (b*100)
cnt = ans//100
cnt = len(str(cnt)) + 2
ans = str(ans)
for i in range(cnt):
    str = ans[i]

print(str)