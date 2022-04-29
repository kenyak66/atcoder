menu = list(int(input()) for _ in range(5))

ans = 0
r = 0
for i in menu:
    ans += i
    if i%10 != 0:
        ans += (10 - i%10)
        if (10 - i%10) > r:
            r = (10 - i%10)
print(ans - r)