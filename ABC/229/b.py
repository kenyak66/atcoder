a, b = map(str, input().split())

flg = True
for i in range(len(a)):
    if int(a[-(i+1)]) + int(b[-(i+1)]) > 9:
        flg = False
        break
print("Easy" if flg else "Hard")