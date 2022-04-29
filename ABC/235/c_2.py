import bisect
n, q = map(int, input().split())
a = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(q)]

cnt = 0
for i in range(q):
    print(a)
    print(a.count(query[i][0]), (query[i][1] - cnt), query[i][0])
    if a.count(query[i][0]) >= (query[i][1] - cnt):
        index = bisect.bisect_left(a, query[i][0])
        print(index+1)
        cnt += 1
        a[index] = 0

    else:
        print(-1)
        continue