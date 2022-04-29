n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
flag = True

for i in range(m):
    if b[i] in a:
        index = b[i]
        a.remove(a[index - 1])
    else:
        flag = False
        break
    
print("Yes" if flag else "No")