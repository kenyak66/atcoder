ans = []

while(True):
    r0, w0, c, r = map(int, input().split())
    if r0 == 0:
        break
    count = 0
    if r0 >= w0:
        while(True):
            if (r0 + r*count)//w0 >= c:
                break
            count += 1
    else:
        while(True):
            if (r0 + r*count)//w0 == c:
                break
            count += 1
    ans.append(count)

for i in ans:
    print(i)