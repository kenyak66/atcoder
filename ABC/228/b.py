n, x = map(int, input().split())
a = list(map(int, input().split()))

l = [False] * n
ans = 0
f = x

while True:
    f -= 1
    if l[f] == False:
        l[f] = True
        ans += 1
        f = a[f]
    else:
        break

print(ans)