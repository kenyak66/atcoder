s = list(input())
k = input()

lim = s.count(".")

ans = 0
cnt = 0
num = 0
first = 0


while s.count("x") > 0:
    num = 0
    for i in range(k):
        cnt += 1
        idx = s.find(".")
        if num == 0:
            first = idx
        num += 1
        s[idx] = "x"
    
    if len(s[:s.find(".")] + 1) > ans:
        ans = len(s[:s.find(".")] + 1)
    
    del s[:first + 1]

print(ans)