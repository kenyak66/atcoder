n = input()

n = n[::-1]
for i in range(len(n)):
    if n[i] != '0':
        n = n[i:len(n)]
        break
if n == n[::-1]:
    print('Yes')
else:
    print('No')