a, b = map(int, input().split())

cnt = 1
ans = a
while ans < b:
    cnt += 1
    ans = a * cnt - (cnt - 1)
print(cnt)