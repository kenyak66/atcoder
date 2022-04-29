n = int(input())
d, x = map(int, input().split())
a = list(int(input()) for _ in range(n))

choco = x
for i in range(n):
    day = 1
    num = 1
    while day <= d:
        choco += 1
        day += num * a[i]

print(choco)