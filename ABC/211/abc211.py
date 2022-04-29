S = str(input())
S_l = list(S)
S_2 = [S_l.count("c"), S_l.count("h"), S_l.count("o"), S_l.count("k"), S_l.count("u"), S_l.count("d"), S_l.count("a"), S_l.count("i")]
ans = 0

if S_l.count("c") == 0:
    print(ans)
elif S_l.count("h") == 0:
    print(ans)
elif S_l.count("o") == 0:
    print(ans)
elif S_l.count("k") == 0:
    print(ans)
elif S_l.count("u") == 0:
    print(ans)
elif S_l.count("d") == 0:
    print(ans)
elif S_l.count("a") == 0:
    print(ans)
elif S_l.count("i") == 0:
    print(ans)
else:
    ans = max(S_2) + 1
print(ans)