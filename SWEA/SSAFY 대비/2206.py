dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 1])
    visit = [[[0] * 2 for i in range(m)] for i in range(n)]
    visit[0][0][1] = 1
    while q:
        x, y, w = q.popleft()
        if x == n - 1 and y == m - 1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mtx[nx][ny] == 1 and w == 1: # 막히고 뚫을 수 있을때
                    visit[nx][ny][0] = visit[x][y][1] + 1
                    q.append([nx, ny, 0])
                elif mtx[nx][ny] == 0 and visit[nx][ny][w] == 0: # 방문 상태 확인
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    q.append([nx, ny, w])
    return -1


n, m = map(int, input().split())
mtx = []
for i in range(n):
    mtx.append(list(map(int, list(input().strip()))))

print(bfs())