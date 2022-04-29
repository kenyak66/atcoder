s1 = input()
s2 = input()

ans = "No"
if s1[0] == s1[1]:
    ans = "Yes"
elif s2[0] == s2[1]:
    ans = "Yes"
elif s1[0] == s2[0]:
    ans = "Yes"
elif s1[1] == s2[1]:
    ans = "Yes"
print(ans)