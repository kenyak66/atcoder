N = int(input())
X, Y = map(int, input().split())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]

ans = 0

if sum(A) < X | sum(B) < Y:
    ans = -1

for i 

print(ans)