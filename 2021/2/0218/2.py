n = int(input())
s = set()

for i in range(n):
    x = input()
    if x not in s:
        print(i+1)
    s.add(x)