n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
rev = False
if sum(a) >= x:
    a.sort()
else:
    a.sort(reverse=True)
    rev = True

for i in a:
    if i <= x:
        x -= i
        ans += 1
    else:
        break
if rev:
    ans -= 1
print(ans)