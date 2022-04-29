a, b = map(int, input().split())
s = input()

flg = True
for i in range(a + b + 1):
    if i != a:
        if s[i] != '-':
            continue
        else:
            flg = False
            break
    else:
        if s[i] == '-':
            continue
        else:
            flg = False
            break
print('Yes' if flg else 'No')