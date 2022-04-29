n, a, b = map(int, input().split())
s = input()
cnt = 0
cntb = 0

for i in range(n):
    flg = True
    if s[i] == "b":
        cntb += 1

    if s[i] == "c":
        flg = False
    if cnt == a + b:
        flg = False
    if cnt < a + b:
        if s[i] == "b":
            if cntb > b:
                flg = False

    if flg:
        cnt += 1
        print("Yes")
    else:
        print("No")
