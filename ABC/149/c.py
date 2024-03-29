def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

x = int(input())

while True:
    if isprime(x):
        print(x)
        break
    x += 1