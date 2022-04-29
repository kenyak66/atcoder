s = list(input())
t = list(input())


if s == t:
    print("Yes")
else:
    ans = "No"
    for i in range (1, len(s)):
        s[i - 1], s[i] = s[i], s[i - 1]
        if s == t:
            ans = "Yes"
        s[i], s[i - 1] = s[i - 1], s[i]
    print(ans)