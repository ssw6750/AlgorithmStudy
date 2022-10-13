import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def value_sum(i, j, n1, mtx):
    value = 0
    visited = []
    queue = deque([[i, j]])
    k = mtx[i][j]

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            y = n[0]
            x = n[1]
            if mtx[y][x] == k:
                value+=mtx[y][x]
                for i in range(4):
                    yy = y+dy[i]
                    xx = x+dx[i]
                    if 0<=yy<n1 and 0<=xx<n1:
                        queue.append([yy, xx])
        
    return value

def dice(F, R, U, d):
    #오른쪽 아래, 왼쪽, 위
    dir = [
        [F, U, 7-R],
        [U, R, 7-F],
        [F, 7-U, R],
        [7-U, R, F]
    ]
    return dir[d]

def move(i, j, dir, dic):
    ii = i+dy[dir]
    jj = j+dx[dir]
    if ii < 0 or ii >= n or jj < 0 or jj >= n:
        dir = (dir+2)%4
        ii = i+dy[dir]
        jj = j+dx[dir]
    # elif jj < 0 or jj >= n:
    #     dir = d+2//4
    #     ii = i+dy[d]
    #     jj = i+dx[d]
    #     dic = dice(dic[0], dic[1], dic[2], direction)
    dic = dice(dic[0], dic[1], dic[2], dir)
    return ii, jj, dir, dic

n, m = map(int, input().split())
answer = 0
mtx = []
for i in range(n):
    mtx.append(list(map(int, input().split())))

direction = 0
d = [2, 3, 1]
_i =0
_j =0 

for _ in range(m):
    _i, _j, direction, d = move(_i, _j, direction, d)
    f = mtx[_i][_j]
    d_f = 7 - d[2]
    answer+=value_sum(_i, _j, n, mtx)
    if d_f > f:
        direction=(direction+1)%4

print(answer)


