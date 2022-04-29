N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

A_min = abs(A[N - 2] - A[N - 1])
B_min = abs(B[N - 2] - B[N - 1])

if A_min > B_min:
    print(B_min)
else:
    print(A_min)
