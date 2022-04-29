N = int(input())
A = list(map(int, input().split()))
B = []

for i in A:
    B.append(i)

B.sort()
C = B[::-1]

print(A.index(C[1]) + 1)

