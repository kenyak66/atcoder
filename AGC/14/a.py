a = list(map(int, input().split()))

b = [a]
count = 0
while True:
    x, y, z = b[len(b)-1][0], b[len(b)-1][1], b[len(b)-1][2]
    if (x%2 != 0) | (y%2 != 0) | (z%2 != 0):
        print(count)
        break
    elif x == y == z:
        print(-1)
        break
    else:
        count += 1
        b.append([((y+z)//2), ((x+z)//2), ((x+y)//2)])