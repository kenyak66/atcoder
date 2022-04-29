a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = list(int(input()) for _ in range(n))

c = [[False]*3 for i in range(3)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if b[i] == a[j][k]:
                c[j][k] = True
                continue

flg = False
if c[0][0] == c[0][1] == c[0][2] == True:
    flg = True
elif c[1][0] == c[1][1] == c[1][2] == True:
    flg = True
elif c[2][0] == c[2][1] == c[2][2] == True:
    flg = True
elif c[0][0] == c[1][0] == c[2][0] == True:
    flg = True
elif c[0][1] == c[1][1] == c[2][1] == True:
    flg = True
elif c[0][2] == c[1][2] == c[2][2] == True:
    flg = True
elif c[0][0] == c[1][1] == c[2][2] == True:
    flg = True
elif c[0][2] == c[1][1] == c[2][0] == True:
    flg = True

print("Yes" if flg else "No")