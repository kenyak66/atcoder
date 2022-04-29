a, b, k = map(int, input().split())

count = a
ans = 0
while count < b:
    ans += 1
    count *= k
print(ans)