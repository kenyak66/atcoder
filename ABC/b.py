s = str(input())

flag = False
if len(set(s)) == len(s):
    if not s.islower():
        if not s.isupper():
            flag = True
print('Yes' if flag else 'No')
