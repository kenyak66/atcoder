import math

S, T = map(int, input().split())
l = []
ans = 0

for i in range(S):
    l.append(math.factorial(i) // (math.factorial(i - 3) * math.factorial(3)))
