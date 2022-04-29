a, b, c = map(int, input().split())

ans = 0

while ans < a:
    ans += c
if ans > b:
    ans = -1
print(ans)