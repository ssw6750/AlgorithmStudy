# 시간 초과

import copy
import sys
from collections import deque
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs():
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if ny == y2 and nx == x2:
                    return 1
                if v[ny][nx] == 0:
                    if mtx[ny][nx] == '.':
                        q.append([ny, nx])
                    v[ny][nx] = 1
    return 0



r, c = map(int, input().split())
ans = 0
l = []
mtx = []
for i in range(r):
    t = list(input().strip())
    for j in range(c):
        if t[j] == 'L':
            l.append([i, j])
    mtx.append(t)
y1, x1, y2, x2 = l[0][0], l[0][1], l[1][0], l[1][1] 

ans = 1
aa = 0
while True:
    q = deque([[y1, x1]])
    v = [[0]*c for _ in range(r)]

    mtx_copy = copy.deepcopy(mtx)
    for i in range(r):
        for j in range(c):
            if mtx[i][j] == 'X':
                for k in range(4):
                    ny = i+dy[k]
                    nx = j+dx[k]
                    if 0<=ny<r and 0<=nx<c:
                        if mtx[ny][nx] == '.':
                            mtx_copy[i][j] = '.'
    mtx = copy.deepcopy(mtx_copy)

    if bfs():
        print(ans)
        break
    ans+=1
