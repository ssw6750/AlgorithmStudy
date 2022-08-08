import sys
from collections import deque
input = sys.stdin.readline  

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

R, C, T = map(int, input().split())
mx = [list(map(int, input().split())) for _ in range(R)]

c = [] # 공청 좌표
ar = [] # 미세먼지 좌표

for i in range(R):
    for j in range(C):
        if mx[i][j] != 0:
            if mx[i][j] ==-1:
                c.append((i, j))
            else : ar.append((i, j))

top = c[0][0]
bot = c[1][0]

for i in range(T): #T초 반복
    tmp1 = []
    for y, x in ar: # 미세먼지 확산 정보누적
        v = mx[y][x]//5
        for j in range(4):
            ny = y+dy[j]
            nx = x+dx[j]
            if ny >= 0 and ny < R and nx >= 0 and nx < C:
                if (ny == top and nx == 0) or (ny == bot and nx == 0): continue
                tmp1.append((ny, nx, v))
                mx[y][x] -= v

    for y, x, v in tmp1: #확산 실행
        if (y == top and x == 0) or (y == bot and x == 0): continue
        mx[y][x] += v

    tmp = [[0]*C for _ in range(R)]       
    tmp[top][0] = -1
    tmp[bot][0] = -1
    for i in range(R):
        for j in range(C):
            if j == 0: # 1열일때
                if i < top-1: #상단부
                    tmp[i+1][j] = mx[i][j]
                elif i > bot+1: # 하단부
                    tmp[i-1][j] = mx[i][j]
            elif j == C-1:
                if i <= top:
                    if i > 0: #상단부
                        tmp[i-1][j] = mx[i][j]
                    elif i == 0:
                        tmp[i][j-1] = mx[i][j]
                elif i >= bot:
                    if i < R-1: # 하단부
                        tmp[i+1][j] = mx[i][j]
                    elif i == R-1:
                        tmp[i][j-1] = mx[i][j]
            else: # 그 외
                if i == 0:
                    tmp[i][j-1] = mx[i][j]
                elif i == top:
                    tmp[i][j+1] = mx[i][j]
                elif i == bot:
                    tmp[i][j+1] = mx[i][j]
                elif i == R-1:
                    tmp[i][j-1] = mx[i][j]
                else: tmp[i][j] = mx[i][j]
    mx = tmp
    ar = []
    for i in range(R):
        for j in range(C):
            if mx[i][j] != 0:
                if mx[i][j] !=-1:
                    ar.append((i, j))

sum = 2
for i in range(R):
    for j in range(C):
        sum+=mx[i][j]
print(sum)
                    


    

