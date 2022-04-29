n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    #print(a[i], a[i]%2)
    if a[i]%2 != 0:
        cnt += 1

if cnt%2 == 0:
    print("YES")
else:
    print("NO")