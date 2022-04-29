def f(a, b):
    f = 4 * a * b + 3 * a + 3 * b
    return f

n = int(input())
s = list(map(int, input().split()))
t = set()
ans = 0

for a in range(1, 1001):
    for b in range(1, 1001):
        t.add(f(a, b))

for i in s:
    if i not in t:
        ans += 1
print(ans)