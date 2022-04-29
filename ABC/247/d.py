from collections import deque

Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

qu = deque()
for i in range(Q):
    if q[i][0] == 1:
        qu.append([q[i][1] * q[i][2], q[i][1], q[i][2]])
    else:
        score = 0
        count = q[i][1]
        while count > 0:
            left = qu.popleft()
            if left[2] >= count:
                qu.appendleft([left[1] * (left[2] - count), left[1], left[2] - count])
                score += left[1] * count
                count = 0
            else:
                score += left[1] * left[2]
                count -= left[2]
        print(score)