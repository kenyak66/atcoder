n = int(input())
k = int(input())
x = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(x[i], abs(k - x[i]))

print(s*2)