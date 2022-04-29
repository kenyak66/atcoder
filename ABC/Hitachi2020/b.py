a, b, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(m)]

ans = min(a) + min(b)
for i in range(m):
    price = a[c[i][0] - 1] + b[c[i][1] - 1] - c[i][2]
    if ans > price:
        ans = price
print(ans)