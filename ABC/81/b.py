n = int(input())
a = list(map(int, input().split()))

ans = 999999
for i in range(n):
    count = 0
    for j in range(1, 40):
        if a[i]%(2**j) == 0:
            count += 1
        else:
            if ans > count:
                ans = count
            continue
print(ans)