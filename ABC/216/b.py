n = int(input())
s = set(input() for _ in range(n))

print("Yes" if len(s) != n else "No")