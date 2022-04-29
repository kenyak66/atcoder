n, m = map(int, input().split())
a = [input() for _ in range(n * 2)]
for i in range(m):
    for j in range(n):
        if a[j * 2 - 1][0][i] == "G":
            if a[j * 2][0][i] == "C":
                for k in range(n):
                    