s = input()

a = (100*(int(s[0])) + 10*(int(s[1])) + (int(s[2])))
b = (100*(int(s[1])) + 10*(int(s[2])) + (int(s[0])))
c = (100*(int(s[2])) + 10*(int(s[0])) + (int(s[1])))

print(a+b+c)