n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
 
num = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if l[i] == l[j]:
            num += 1
 
print(n - num)