n = int(input())
a = list(map(int, input().split()))

ans1 = []
ans2 = []

for i in range(n):
    ans1.append([a[i], i+1])

ans1.sort()

for i in range(n):
    ans2.append(ans1[i][1])
print(*ans2)