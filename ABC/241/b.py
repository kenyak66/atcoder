from bisect import bisect, bisect_left, bisect_right


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
flag = True

for i in range(m):
    if b[i] >= a[0]:
        index = bisect_left(a, b[i])
    else:
        index = bisect_right(a, b[i])
    
    if index == len(a):
        index = len(a) - 1
    
    if a[index] == b[i]:
        a.remove(a[index])
    else:
        flag = False
        break
    
print("Yes" if flag else "No")