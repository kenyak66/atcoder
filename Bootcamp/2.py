n = int(input())
x = list(map(int, input().split()))

min = sum([k * k for k in x])
new = 0
for i in range(max(x)+1):
    new = sum([(j-i) * (j-i) for j in x])
    if new < min:
        min = new
print(min)