w = input()

flag = True
for i in w:
    if w.count(i)%2 != 0:
        flag = False
        break
print('Yes' if flag else 'No')