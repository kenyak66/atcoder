import math

a, b = map(str, input().split())

ab = int(a+b)
flg = False

for i in range(int(math.sqrt(ab)) + 1):
    if i*i == ab:
        flg = True

print("Yes" if flg else "No")