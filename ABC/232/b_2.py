s = input()
t = input()

cnt = ord(t[0]) - ord(s[0])
if ord(t[0]) < ord(s[0]):
    cnt = ord(t[0]) + 26 - ord(s[0])
cnt_i = 0
flg = True

for i in range(1, len(s)):
    cnt_i = ord(t[i]) - ord(s[i])
    if ord(t[i]) < ord(s[i]):
        cnt_i = ord(t[i]) + 26 - ord(s[i])
    if cnt != cnt_i:
        flg = False
        break
    
print("Yes" if flg else "No")
