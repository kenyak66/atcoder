n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
 
ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            #print(point[i], point[j], point[k])
            if point[j][0] == point[i][0]:
                if point[k][0] != point[i][0]:
                    ans += 1
            else:
                if point[k][0] == point[i][0]:
                    ans += 1
                elif (point[j][1] - point[i][1]) * (point[k][0] - point[i][0]) != (point[k][1] - point[i][1]) * (point[j][0] - point[i][0]):
                    ans += 1
print(ans)