S, T = map(str, input().split())
l = []

l.append(S)
l.append(T)
l.sort()

if l[0] == S:
    print("Yes")
else:
    print("No")