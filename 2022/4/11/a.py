a, b = map(int, input().split())

ans = 0
if a > 12:
    ans = b
elif a > 5:
    ans = b//2
print(ans)