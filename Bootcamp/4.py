n = int(input())

ans = (n * 100) // 108
if int(ans * 1.08) != n:
    ans += 1
    if int(ans * 1.08) != n:
        ans = str(":(")
print(ans)