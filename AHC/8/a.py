from queue import Queue

# 入力
stp = list(map(float, input().split()))
h = [input() for _ in range(20)]
v = [input() for _ in range(19)]

# 迷路作成
maze = [[0]*41 for _ in range(41)]
maze[0], maze[40] = [1]*41, [1]*41
for i in range(41):
    maze[i][0], maze[i][40] = 1, 1
for i in range(20):
    for j in range(19):
        if (h[i])[j] == '1':
            maze[(i+1)*2-2][(j+1)*2], maze[(i+1)*2-1][(j+1)*2], maze[(i+1)*2][(j+1)*2] = 1, 1, 1
for i in range(19):
    for j in range(20):
        if (v[i])[j] == '1':
            maze[(i+1)*2][(j+1)*2-2], maze[(i+1)*2][(j+1)*2-1], maze[(i+1)*2][(j+1)*2] = 1, 1, 1

# 迷路出力
for i in range(41):
    print(maze[i])

visited = [[False] * 41 for i in range(41)]
que = Queue()
costs = [[999999] * 41 for i in range(41)]

# スタート、ゴールの設定
start = [int(stp[0])*2-1, int(stp[1])*2]
goal = maze[int(stp[2])*2-1][int(stp[3])*2]
que.put(start)
costs[start]

while not que.empty():
    x, y = que.get()

    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        x2, y2 = x + dx, y + dy

        # スキップ
        if maze[x2][y2] == 1:
            continue
        if visited[x2][y2] == True:
            continue

# 出力する値
ans = []

# 出力
# print(*ans)