n, m = map(int, input().split())
a = [(input(), _ + 1, m) for _ in range(n * 2)]
b = [_ for _ in range(n * 2)]
for i in range(m):
    for j in range(n):
        a[j * 2 - 1] = list(j * 2 - 1)
        
        if a[j * 2 - 1][0][i] == "G":
            if a[j * 2][0][i] == "C":
                a[j * 2 - 1][2] -= 1
            elif a[j * 2][0][i] == "P":
                a[j * 2][2] -= 1
        elif a[j * 2 - 1][0][i] == "C":
            if a[j * 2][0][i] == "P":
                a[j * 2 - 1][2] -= 1
            elif a[j * 2][0][i] == "G":
                a[j * 2][2] -= 1
        elif a[j * 2 - 1][0][i] == "P":
            if a[j * 2][0][i] == "G":
                a[j * 2 - 1][2] -= 1
            elif a[j * 2][0][i] == "C":
                a[j * 2][2] -= 1
    a.sort(key=lambda x: x[2])
for i in range(n * 2):
    print(a[i][1])