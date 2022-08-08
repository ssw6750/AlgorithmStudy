import sys
from collections import deque
input = sys.stdin.readline  

dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
mx = [list(map(int, input().split())) for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(m)]
c = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for i in range(m): # 이동 정보 순회
    v = [[0]*n for _ in range(n)] 
    for y, x in c:  # 구름 이동
        ny = (y + dy[arr[i][0]-1]*arr[i][1])%n
        nx = (x + dx[arr[i][0]-1]*arr[i][1])%n
        mx[ny][nx] += 1
        v[ny][nx] = 1

    for i in range(n): # 비 복사
        for j in range(n):
            if v[i][j] == 1:
                for k in range(4):
                    ny = i+dy[k*2+1]
                    nx = j+dx[k*2+1]
                    if (ny >= 0 and ny < n) and (nx >=0 and nx < n):
                        if mx[ny][nx] > 0:
                            mx[i][j] += 1

    c = []
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                if mx[i][j] >= 2:
                    mx[i][j] -= 2
                    c.append((i, j))

sum = 0
for i in range(n):
    for j in range(n):
        sum += mx[i][j]

print(sum)
                 






