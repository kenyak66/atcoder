ans = []

def up(u, d, i, cu, count):
    if i not in cu:
        cu.append(i)
        if len(cu) == 2:
            cu = []
            if u == d:
                count += 1

def down(u, d, i, cd, count):
    if i not in cd:
        cd.append(i)
        if len(cd) == 2:
            cu = []
            if u == d:
                count += 1

while(True):
    n = int(input())
    if not n:
        break
    step = list(map(str, input().split()))

    cu = []
    cd = []

    u = 0
    d = 0
    count = 0
    
    for i in range(n):
        if step[i] == 'lu':
            up(u, d, 'lu', cu, count)
        elif step[i] == 'ru':
            up(u, d, 'lu', cu, count)
        elif step[i] == 'ru':
            up(u, d, 'ld', cu, count)
        elif step[i] == 'ld':
            up(u, d, 'rd', cu, count)
    ans.append(count)
    print(ans)

for i in ans:
    print(i)