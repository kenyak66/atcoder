X = list(input())
ans = 0

if X.count(X[0]) == 4:
    ans = 3

for i in range(3):
    a = int(X[i])
    b = int(X[i + 1])

    if b == a + 1:
        ans += 1
    elif b == a - 9:
        ans += 1

if ans == 3:
    print("Weak")
else:
    print("Strong")