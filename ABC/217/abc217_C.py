N = int(input())
p = list(map(int, input().split()))
l1 = []
l2 = []

for i in range(N):
    l1.append([p[i], i])

for j in range(N):
    for k in range(N):
        if l1[k][0] == j + 1:
            l2.append(str(l1[k][1] + 1))

print(' '.join(l2))