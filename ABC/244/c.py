n = int(input())
num = []
for i in range(1, 2*n + 2):
    num.append(i)

print(num[0])
num.remove(num[0])

for i in range(2*n + 1):
    a = int(input())
    num.remove(a)
    b = num[0]
    print(b, flush=True)
    num.remove(b)