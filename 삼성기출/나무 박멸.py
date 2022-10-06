import sys
input = sys.stdin.readline
from copy import deepcopy

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

dy2 = [1, 1, -1, -1]
dx2 = [1, -1, 1, -1]

# 제초
def weeding(i, j, k):
    df = []
    if mtx[i][j] > 0:
        die_cnt=mtx[i][j] # 죽는 나무의 수
    else: die_cnt = 0
    for o in range(1, k+1):
        for t in range(4):
            if t in df:
                continue
            yy = i+o*dy2[t]
            xx = j+o*dx2[t]
            if 0 <= yy < n and 0 <= xx < n:
                if mtx[yy][xx] == 0 or mtx[yy][xx] == -1:
                    df.append(t)
                else: die_cnt+=mtx[yy][xx]
    return die_cnt



n, m, k, c = map(int, input().split())
mtx = [list(map(int, input().split())) for _ in range(n)]
v = [[0 for _ in range(n)] for _ in range(n)]

all_cnt = 0
for y in range(m):
    # 성장 (인접한 나무에 영향)
    for i in range(n):
        for j in range(n):
            if mtx[i][j] > 0: #나무
                adj_cnt = 0
                for o in range(4):
                    yy = i+dy[o]
                    xx = j+dx[o]
                    if 0 <= yy < n and 0 <= xx < n:
                        if mtx[yy][xx] > 0:
                            adj_cnt +=1
                mtx[i][j] += adj_cnt

    # 번식
    mtx_copy = deepcopy(mtx)
    for i in range(n):
        for j in range(n):
            if mtx[i][j] > 0: #나무
                emt_cnt = 0
                for o in range(4):
                    yy = i+dy[o]
                    xx = j+dx[o]
                    if 0 <= yy < n and 0 <= xx < n:
                        if mtx[yy][xx] == 0:
                            emt_cnt +=1
                if emt_cnt > 0:
                    bre = mtx[i][j]//emt_cnt

                    for o in range(4):
                        yy = i+dy[o]
                        xx = j+dx[o]
                        if 0 <= yy < n and 0 <= xx < n:
                            if mtx[yy][xx] == 0:
                                mtx_copy[yy][xx]+=bre
    mtx = deepcopy(mtx_copy)

    # 제초가 가장 많이 발생하는 지역 찾기
    mx = [[],0]
    for i in range(n):
        for j in range(n): 
            if mtx[i][j] != 0 and mtx[i][j] !=-1:
                tmp = weeding(i, j, k)
                if mx[1] < tmp:
                    mx = [[i, j], tmp]  
    all_cnt+=mx[1]  
              

    # 이전 제초의 남아있는 년수 감소
    for i in range(n):
        for j in range(n):
            if mtx[i][j] <= -2:
                mtx[i][j]+=2


    # 제초
    mtx[mx[0][0]][mx[0][1]] = -2
    for o in range(1, k+1):
            for t in range(4):
                yy = mx[0][0]+o*dy2[t]
                xx = mx[0][1]+o*dx2[t]
                if 0 <= yy < n and 0 <= xx < n:
                    mtx[yy][xx] = -2*c


print(all_cnt)