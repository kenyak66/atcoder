
S, K = map(str, input().split())
K = int()
l = list(S)

sorted(l)
l1 = []


if l.length() == 1:
    l1.append(S)
else:
    for i in range(l.length()):
        if i != 0:
            l[0], l[i] = l[i], l[0]
        for j in range(l.length() - 1):
        
sorted(l1)
print(l1[K - 1])
