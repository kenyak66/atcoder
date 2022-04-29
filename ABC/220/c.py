n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum = sum(a)
ans = (x // sum) * n
num = x // sum
x %= sum
for i in a:
    num += i
    ans += 1
    if num > x:
        break
print(ans)