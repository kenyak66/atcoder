def collatz(x):
    count = 1
    while x > 2:
        count += 1
        if x%2 == 0:
            x //= 2
        else:
            x = 3*x + 1
    return count

s = int(input())
if s <= 2:
    print(4)
else:
    print(collatz(s) + 2)