n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(int(input()) for _ in range(q))

a.sort()
a = a[::-1]

for i in x:
    left = 0
    right = n

    while(left != right):
        mid = (left + right) // 2

        if(a[mid] < i):
            right = mid
        else:
            left = mid + 1

    ans = left
    print(ans)