N = int(input())
S = str(input())
S_list = list(S)
S_list2 = list(map(int, S_list))
result = 0
lim = 0

while lim != 1:
    for i in range(N):
        if  S_list2[i] == 1:
            result = i
            lim += 10
print(result)
if result % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")


