n = int(input())
s = list(map(int, input().split()))

s.sort()
cnt = []

for i in range(300):
    for j in range(300):
        if 4 * i * j + 3 * (i + j) > s[-1]:
            break
        for k in s:
            if 4 * i * j + 3 * (i + j) == k:
                cnt.append(k)
                break
    if len(set(cnt)) == len(s):
        break

ans = set(cnt)
print(len(s) - len(ans))
print(set(cnt), cnt, s)