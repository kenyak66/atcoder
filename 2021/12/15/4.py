abcd = list(map(int, list(input())))
pm = ["+", "-"]

ans = abcd[0]
for i in range(2):
    if i == 0:
        ans += abcd[1]
    else:
        ans -= abcd[1]

    for j in range(2):
        if i == 0:
            ans += abcd[2]
        else:
            ans -= abcd[2]

        for k in range(2):
            if i == 0:
                ans += abcd[3]
            else:
                ans -= abcd[3]
        
        if ans == 7:
            print(str(abcd[0]) + pm[i] + str(abcd[1]) + pm[j] + str(abcd[2]) + pm[k] + str(abcd[3]) + "=" + ans)