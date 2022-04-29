h, w = map(int, input().split())
c = list(list(str(input())) for _ in range(h))

for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            num  = ['1', '2', '3', '4', '5']
            if i != 0:
                if c[i-1][j] in num:
                    num.remove(c[i-1][j])
            if i != h-1:
                if c[i+1][j] in num:
                    num.remove(c[i+1][j])
            if j !=0:
                if c[i][j-1] in num:
                    num.remove(c[i][j-1])
            if j != w-1:
                if c[i][j+1] in num:
                    num.remove(c[i][j+1])
            c[i][j] = num[0]
for i in c:
    print(''.join(i))