n = int(input())
s = list(input() for _ in range(n))

set = set(s)
ans = ""
max_cnt = 0

for i in set:
    cnt = 0
    for j in s:
        if j == i:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        ans = i

print(ans)