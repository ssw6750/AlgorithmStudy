dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

from collections import defaultdict
import sys
input = sys.stdin.readline
from copy import deepcopy

n = int(input())
ar = []
d = defaultdict()
for _ in range(n*n):
    tmp = list(map(int, input().split()))
    d[tmp[0]] = tmp[1:]
    ar.append(tmp)
mtx = [[0]*n for _ in range(n)]

for s in range(n*n):
    mx = [-1, -1, [0, 0]]
    for i in range(n):
        for j in range(n):
            if mtx[i][j] > 0:
                continue
            cnt = 0
            em_cnt = 0
            for k in range(4):
                di = i+dy[k]
                dj = j+dx[k]
                if 0<= di < n and 0<= dj <n:
                    if mtx[di][dj] in ar[s][1:]:
                        cnt+=1
                    elif mtx[di][dj] == 0:
                        em_cnt+=1
            if cnt > mx[0]:
                mx = [cnt, em_cnt, [i, j]]
            elif cnt == mx[0]:
                if em_cnt > mx[1]:
                    mx = [cnt, em_cnt, [i, j]]
    mtx[mx[2][0]][mx[2][1]] = ar[s][0]

score = [0, 1, 10, 100, 1000]
ans = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(4):
            di = i+dy[k]
            dj = j+dx[k]
            if 0<= di < n and 0<= dj <n:
                if mtx[di][dj] in d[mtx[i][j]]:
                    cnt+=1
        ans += score[cnt]

print(ans)