s1 = input()
s2 = input()
s3 = input()
t = input()

T = list(t)
list = []

for i in T:
    if i == '1':
        list.append(s1)
    elif i == '2':
        list.append(s2)
    else:
        list.append(s3)

print(''.join(list))