n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]

p2 = []

for i in p:
    p2.append(sum(i))

p3 = sorted(p2)

for j in p2:
    if (j >= p3[-k] - 300):
        print("Yes")
    else:
        print("No")