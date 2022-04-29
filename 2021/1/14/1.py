k = int(input())
a, b = map(int, input().split())

flg = False

if a == b:
    if a%k == 0:
        flg = True

for i in range(a, b+1):
    if i%k == 0:
        flg = True
        break

print("OK" if flg else "NG")