n, s, d = map(int, input().split())
magic = [list(map(int, input().split())) for _ in range(n)]

flag = False
for i in range(n):
    if magic[i][0] < s:
        if magic[i][1] > d:
            flag = True
            break
print('Yes' if flag else 'No')