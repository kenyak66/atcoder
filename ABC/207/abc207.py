N, M = map(int, input(). split())
l = [list(map(int, input().split())) for l in range(M)]

for i in range(M):
    m = i
    for j in range(i + 1, M):
        if l[j][0] < l[m][0]:
            l[j], l[m] = l[m], l[j]
            m = j
        elif l[j][0] == l[m][0]:
            if l[j][1] < l[m][1]:
                l[j], l[m] = l[m], l[j]
            m = j
print(l)


