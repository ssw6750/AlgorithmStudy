dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(rr, cc):
    if v[rr][cc]: # 방문했다면
        return
    else:
        snapshot[rr][cc] = idx
        v[rr][cc] = 1

        # 하단과 연결되어 있으면 
        if rr == r-1: 
            not_separate.append(idx)

        for k in range(4):
            ny = rr+dy[k]
            nx = cc+dx[k]
            if 0 <= ny < r and 0<= nx <c:
                if mtx[ny][nx] == 'x':
                    dfs(ny, nx)


def search_cluster():
    global idx
    for s in range(r):
        for o in range(c):
            if v[s][o]: # 방문했다면
                continue
            if mtx[s][o] == '.':
                v[s][o] = 1
                continue
            else:
                dfs(s, o)
                idx+=1


r, c = map(int, input().split())
mtx = []
for i in range(r):
    mtx.append(list(input().strip()))

n = int(input())
ar = list(map(int, input().split()))

d = 1 # 방향 1 : 왼쪽 , 0 : 오른쪽

for i in range(n):

    # 막대 던지기
    h = ar[i]
    if d:
        for j in range(c):
            if mtx[r-h][j] == 'x':
                mtx[r-h][j] = '.'
                break
    else:
        for j in range(c-1, -1, -1):
            if mtx[r-h][j] == 'x':
                mtx[r-h][j] = '.'
                break
    d = 1-d

    v = [[0]*c for _ in range(r)]
    snapshot = [[0]*c for _ in range(r)]
    idx = 1 # 클러스터 인덱스
    not_separate= [] # 분리되지 않은 클러스터의 인덱스

    # 분리된 클러스터 처리
    search_cluster()
    not_separate.sort()
    not_separate = list(set(not_separate))
    

    for j in range(1, idx):
        if j not in not_separate:
            # 분리되어 있음

            # 떨어지는 높이 찾기
            mn = 101
            for ii in range(r-2, -1, -1):
                for jj in range(c):
                    if snapshot[ii][jj] == j:
                        h=0
                        for kk in range(ii+1, r):                       
                            if kk == r-1:
                                h+=1
                                break
                            if snapshot[kk][jj] != 0 and snapshot[kk][jj] != j:
                                break
                            h+=1
                        if mn > h:
                            mn = h
                        
            # 떨어트리기
            for ii in range(r):
                for jj in range(c):
                    if snapshot[ii][jj] == j:
                        if snapshot[ii-mn][jj] != j: #떨어진 미네랄은 포함 x
                            mtx[ii][jj] = '.'
                        mtx[ii+mn][jj] = 'x'

                                 

for i in range(r):
    for j in range(c):
        print(mtx[i][j], end='')
    print()

            

