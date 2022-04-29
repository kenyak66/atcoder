n, m = map(int, input().split())
a = list(map(float, input().split()))

a.sort()

a2 = a[::-1]

cnt = 0
s = sum(a2)

for i in a2:
    if i*(4*m) >= s:
        cnt += 1
    else:
        break

print("Yes" if cnt >= m else "No")