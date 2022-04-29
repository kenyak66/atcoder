s = input()
ans = []

for i in range(len(s)):
    s = s[1:] + s[0]
    ans.append(s)
ans.sort()
print(ans[0])
print(ans[len(s) - 1])
