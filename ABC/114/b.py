s = input()

ans = []
for i in range(len(s)-2):
    x = abs(753 - int(s[i:i+3]))
    ans.append(x)
print(min(ans))