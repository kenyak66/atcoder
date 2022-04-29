n, k = map(int, input().split())
s = list(str(input()) for _ in range(n))

ans = []
for i in range(n):
    for j in range(len(s[i])):
        if s[i][j] in ans:
            continue
        else:
            count = 1
            for l in range(i+1, n):
                if s[i][j] in s[l]:
                    count += 1
        if count == k:
            ans.append(s[i][j])

fans = 0
for i in range(n):
    num = 0
    for al in ans:
        if al in s[i]:
            ans.remove(al)
            num += 1
    if num!= 0:
        fans += 1
    if len(ans) == 0:
        break
print(fans)