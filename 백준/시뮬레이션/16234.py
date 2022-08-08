# 80퍼

import sys
from collections import deque
input = sys.stdin.readline  

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def BFS(i, j):
    que = deque()
    que.append((i, j))
    v[i][j] = True
    tmp = [(i, j)]
    sum = arr[i][j]
    s = 1
    while que:
        y1, x1 = que.popleft()
        for i in range(4):
            y = y1 + dy[i]
            x = x1 + dx[i] 
            if y >= 0 and y < N and x >= 0 and x < N and v[y][x] == False:
                a = abs(arr[y1][x1] - arr[y][x])
                if a >= L and a <= R:
                    v[y][x] = True
                    sum += arr[y][x]
                    s+=1
                    tmp.append((y, x))
                    que.append((y, x))
    c=sum//s
    for x, y in tmp:
        arr[x][y] = c    

    return (len(tmp))             
                    
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d=0 #날짜
while True:
    f=False
    v = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j] == False:
                if BFS(i, j) > 1:
                    f = True
    if f == False: break
    d+=1

print(d)
