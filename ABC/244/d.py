s = list(map(str, input().split()))
t = list(map(str, input().split()))

flg = False
if t[0] == s[0]:
    if t[1] == s[1]:
        if t[2] == s[2]:
            flg = True
elif t[0] == s[1]:
    if t[1] == s[2]:
        if t[2] == s[0]:
            flg = True
elif t[0] == s[2]:
    if t[1] == s[0]:
        if t[2] == s[1]:
            flg = True

print('Yes' if flg else 'No')