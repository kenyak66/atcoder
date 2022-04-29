P = list(map(int, input().split()))

A = "abcdefghijklmnopqrstuvwxyz"
A_list = list(A)
ans =[]

for i in P:
    ans.append(A_list[i - 1])

print(''.join(ans))