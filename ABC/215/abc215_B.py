N = int(input())
k = 0

while 2**k <= N:
    k += 1
    if 2**k > N:
        k -= 1
        break
print(k)