n = int(input())
s = input()

max = 0
count = 0
for i in s:
    if i == 'I':
        count += 1
        if count > max:
            max = count
    else:
        count -= 1
print(max)