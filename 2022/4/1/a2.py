ans = []

while(True):
    n = int(input())
    if n == 0:
        break
    step = list(map(str, input().split()))

    count = 0
    right = 0
    left = 0

    for i in step:
        if i == 'lu':
            left += 1
            if right == 1:
                count += 1
                right, left = 0, 0
        if i == 'ru':
            right += 1
            if left == 1:
                count += 1
                right, left = 0, 0
        if i == 'ld':
            left -= 1
            if right == -1:
                count += 1
                right, left = 0, 0
        if i == 'rd':
            right -= 1
            if left == -1:
                count += 1
                right, left = 0, 0
    ans.append(count)

for i in ans:
    print(i)