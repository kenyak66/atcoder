n = int(input())

ans = n
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if j == 1:
            continue
        for k in range(j, n + 1):
            if i * j * k <= n:
                ans += 1
                print(i, j, k)
print(ans)