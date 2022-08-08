

import sys
from collections import deque
input = sys.stdin.readline  

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and mx[nx][ny] == 0:
                mx[nx][ny] = mx[x][y] + 1
                que.append([nx, ny])

m, n = map(int, input().split())
mx = [list(map(int, input().split())) for _ in range(n)]
que = deque([])
res = 0

for i in range(n):
    for j in range(m):
        if mx[i][j] == 1:
            que.append([i, j])

bfs()
for i in mx:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)