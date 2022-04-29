a, b = map(int, input().split())
ans = 1
for i in range(a - b):
    ans *= 32
print(ans)