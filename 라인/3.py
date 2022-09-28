# 시간이 10억분 주어지지만 방문하는 격자는 최대 30*30


from collections import deque

# n=3; m=2; fires=[[1,1]]; ices=[[3,3]]
n=5; m=1000000000; fires=[[5,5], [1,3], [5,2]]; ices=[[1,5],[3,2]]


dx = [0, 0, -1, 1, 1, 1, -1, -1] # (0~3) 상하좌우 (4~7) 대각 4방향
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def fire(y, x, mt, t, nn): # 좌표, 주어진 배열, 시간, nn = 가로길이 = 세로길이
    visited = []
    queue = deque([[[y, x], t+1]])
    mt[y][x] -=1 # 정가운데 0분일때 고려 x

    while queue:
        n = queue.popleft()
        if n[0] not in visited and n[1] > 0: # 방문하지 않고 시간이 0분 이상 남았을때
            y1 = n[0][0]
            x1 = n[0][1]
            visited.append(n[0])
            mt[y1][x1] += n[1]
            for i in range(8):
                yy=y1+dy[i]
                xx=x1+dx[i]
                if 0<= yy < nn and 0<= xx < nn:
                    queue.append([[yy, xx], n[1]-1])


def ice(y, x, mt, t, nn):
    visited = []
    queue = deque([[[y, x], t+1]])
    mt[y][x] +=1

    while queue:
        n = queue.popleft()
        if n[0] not in visited and n[1] > 0:
            y1 = n[0][0]
            x1 = n[0][1]
            visited.append(n[0])
            mt[y1][x1] -= n[1]
            for i in range(4):
                yy=y1+dy[i]
                xx=x1+dx[i]
                if 0<= yy < nn and 0<= xx < nn:
                    queue.append([[yy, xx], n[1]-1])


def solution(n, m, fires, ices):
    mt = [[0 for _ in range(n)] for _ in range(n)]
    for i in fires:
        fire(i[0]-1, i[1]-1, mt, m, n) #배열이 (1,1)에서 시작
    for i in ices:
        ice(i[0]-1, i[1]-1, mt, m, n)

    print(mt)

solution(n, m, fires, ices)