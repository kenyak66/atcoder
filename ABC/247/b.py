n = int(input())
l = [list(map(str, input().split())) for _ in range(n)]

flag = True
for i in range(n):
    count = 0
    for j in range(n):
        if j == i:
            continue

        if l[i][0] == l[j][0]:
            count += 1
        elif l[i][0] == l[j][1]:
            count += 1

        if l[i][1] == l[j][0]:
            count += 1
        elif l[i][1] == l[j][1]:
            count += 1

        if count == 2:
            flag = False
            break
        
print('Yes' if flag else 'No')