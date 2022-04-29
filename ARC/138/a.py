import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))
inf = 9999999999999999999999

l = []
for i, j in enumerate(a):
    l.append((j, -i))#後でheapqを使うときの都合で-iにする
l.sort()

hq = []
heapq.heapify(hq)

ans = inf
flag = False

for (j, i) in l:
    if -i >= k:
        if flag:
            p = heapq.heappop(hq)
            ans = min(ans, -i + p)
            heapq.heappush(hq, p)
    else:
        flag = True
        heapq.heappush(hq, i)

print(ans if ans != inf else -1)