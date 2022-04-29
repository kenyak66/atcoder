n = int(input())
a = list(map(int, input().split()))
a.sort()
a = set(a)
for i in range(2002):
    if i not in a:
        print(i)
        break