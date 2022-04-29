n = int(input())
music = [list(map(str, input().split())) for _ in range(n)]
x = input()

flag = False
ans = 0
for i in range(n):
    if flag:
        ans += int(music[i][1])
        continue
    if music[i][0] == x:
        flag = True
print(ans)