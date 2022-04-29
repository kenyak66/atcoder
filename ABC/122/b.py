s = list(input())

count = 0
ans = 0

for i in s:
    if i == "A":
        count += 1
    elif i == "C":
        count += 1
    elif i == "G":
        count += 1
    elif i == "T":
        count += 1
    else:
        count = 0
    
    if ans < count:
        ans = count

print(ans)