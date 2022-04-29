def right(i):
    flg = True
    for i in range(m):

        if tonari[l[i][0] - 1] == 0:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 1, 2
            elif tonari[l[i][1] - 1] == 1:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 1, 3
            elif tonari[l[i][1]- 1] == 2:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 2, 3
            else:
                flg = False
                break

        elif tonari[l[i][0] - 1] == 1:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 1
            if tonari[l[i][1] - 1] == 2:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 3
            else:
                flg = False
                break
        
        elif tonari[l[i][0] - 1] == 2:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 2
            if tonari[l[i][1] - 1] == 1:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 3
            else:
                flg = False
                break

        elif tonari[l[i][0] - 1] == 3:
            flg = False
            break

    return flg

def left(i):
    flg = True
    for i in range(m):

        if tonari[l[i][0] - 1] == 0:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 2, 1
            elif tonari[l[i][1] - 1] == 1:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 1, 3
            elif tonari[l[i][1]- 1] == 2:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 2, 3
            else:
                flg = False
                break

        elif tonari[l[i][0] - 1] == 1:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 1
            if tonari[l[i][1] - 1] == 2:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 3
            else:
                flg = False
                break
        
        elif tonari[l[i][0] - 1] == 2:
            if tonari[l[i][1] - 1] == 0:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 2
            if tonari[l[i][1] - 1] == 1:
                tonari[l[i][0] - 1], tonari[l[i][1] - 1] = 3, 3
            else:
                flg = False
                break

        elif tonari[l[i][0] - 1] == 3:
            flg = False
            break

    return flg


n, m = map(int, input().split())
l = [list(map(int, input().split())) for l in range(m)]

tonari = [0]*n

#0:右左どちらも開いてる
#1:右のみ埋まってる
#2:左のみ埋まってる
#3:右左どちらも埋まってる

flg = True
for i in range(m):


print("Yes" if flg else "No")