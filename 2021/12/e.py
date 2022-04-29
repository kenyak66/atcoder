x, k = map(int, input().split())

kx = k*x

for i in range(1, kx):
    if i(i + 1)/2 == kx:
        print(i)
        break
    elif i(i + 1)/2 > kx:
        print("None")
        break