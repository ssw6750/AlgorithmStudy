dy = [0, -1, -1, -1,  0,  1, 1, 1]
dx = [1,  1,  0, -1, -1, -1, 0, 1]

import sys
input = sys.stdin.readline
from copy import deepcopy

n, m = tuple(map(int, input().split()))
mtx = []
for i in range(n):
    mtx.append(list(map(int, input().split())))

c = []
for i in range(m):
    c.append(list(map(int, input().split())))

f = [[False for _ in range(n)] for _ in range(n)]

for i in range(n - 2, n):
    for j in range(2):
            f[i][j] = True

for t in range(m):
    d, p = c[t][0]-1, c[t][1]

    # 성장제 이동
    copy_f = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if f[i][j]:
                di = (i+dy[d]*p)%n
                dj = (j+dx[d]*p)%n
                copy_f[di][dj] = True
                mtx[di][dj] +=1
    f = deepcopy(copy_f)
    # 성장
    copy_mtx = deepcopy(mtx)
    for i in range(n):
        for j in range(n):
            if f[i][j]:
                cnt = 0
                for k in range(4):
                    di = i+dy[(k*2)+1]
                    dj = j+dx[(k*2)+1]
                    if 0<=di<n and 0<=dj<n:
                        if copy_mtx[di][dj] > 0:
                            cnt+=1
                mtx[i][j]+=cnt

    # 성장제 위치 지정
    for i in range(n):
        for j in range(n):
            if not f[i][j]:
                if mtx[i][j] >= 2:
                    mtx[i][j] -= 2
                    f[i][j] = True
            else: f[i][j] = False

ans = 0
for i in range(n):
    for j in range(n):
        ans+=mtx[i][j]

print(ans)

