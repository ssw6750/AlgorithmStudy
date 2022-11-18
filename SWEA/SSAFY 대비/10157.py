import sys
input = sys.stdin.readline


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dy1 = [1, 0, -1, 0]
dx1 = [0, 1, 0, -1]

c, r = map(int, input().split())
k = int(input())
v = [[0] * c for _ in range(r)]

if k > r*c:
    print(0)
    sys.exit()

cnt = 1 
dir = 0 

x = 0
y = r-1

xx = 1
yy = 1

while True:
    if cnt == k:
        print(xx, yy)
        break
    v[y][x] = cnt
    nx = x+dx[dir]
    ny = y+dy[dir]
    if nx < 0 or ny < 0 or nx >= c or ny >= r or v[ny][nx] != 0:
        dir = (dir+1) % 4 
        nx = x+dx[dir]
        ny = y+dy[dir]

    xx = xx+dx1[dir]
    yy = yy+dy1[dir]
    x = nx
    y = ny
    cnt += 1