s = input()
t = input()

alphabet = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

flg = True
ans = True
cnt = 0

cnt_1 = 0
cnt_2 = 0

for _ in range(len(s)):
    for i in range(32):
        if flg:
            if alphabet[i] == s[_]:
                cnt_1 = i
                flg = False
        else:
            if alphabet[i] == t[_]:
                cnt_2 = i
                flg = True
                print(s[_] + str(cnt_1), t[_] + str(cnt_2), cnt_2 - cnt_1, cnt)

                if _ == 0:
                    cnt = cnt_2 - cnt_1
                else:
                    if cnt != cnt_2 - cnt_1:
                        ans = False
                        break
                    else:
                        continue

print("Yes" if ans else "No")
