n, m = map(int, input().split())
p = list(map(input().split()))

a = 0
b = 0
cnt = 0

for i in p:
    cnt += 1

    if i == "A":
        a += 1
    else:
        b += 1
    
    if a >= m:
        if a - b >= 2:
            print("A " + cnt)
            break

    if b >= m:
        if b - a >= 2:
            print("B " + cnt)
            break

if a - b < 2:
    print(-1)