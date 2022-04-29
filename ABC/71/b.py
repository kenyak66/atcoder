s = list(str(input()))

abc = list('abcdefghijklmnopqrstuvwxyz')
s = set(s)
for i in s:
    abc.remove(i)

if len(abc) != 0:
    print(abc[0])
else:
    print('None')