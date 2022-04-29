q = int(input())
t = [list(map(int, input().split())) for _ in range(q)]

ans = []
for i in range(q):
    if t[i][0] == 1:
        ans.insert(0, t[i][1])
    elif t[i][0] == 2:
        ans.append(t[i][1])
    else:
        print(ans[t[i][1]-1])