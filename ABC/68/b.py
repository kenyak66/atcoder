n = int(input())

ans = 1
i = 0
while ans < n:
    i += 1
    ans = 2**i
    if ans > n:
        ans //= 2
        break

print(ans)