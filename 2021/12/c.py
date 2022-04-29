x, a = map(int, input().split())

for i in range(a):
    x -= 1
    if x == 0:
        x = 12

print(x)