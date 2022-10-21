dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# import sys
# input = sys.stdin.readline

for t in range(int(input())) :
    n = int(input())

    mtx = [[0] * n for _ in range(n)]

    x, y = 0, 0
    dir = 0

    for j in range(1, n * n + 1) :
        mtx[x][y] = j
        x += dx[dir]
        y += dy[dir]

        if not 0 <= x < n or not 0 <= y < n or mtx[x][y] != 0 :
            x -= dx[dir]
            y -= dy[dir]
            dir = (dir + 1) % 4
            x += dx[dir]
            y += dy[dir]

    print('#{} '.format(t+1))
    for i in range(n) :
        for j in range(n) :
            print(mtx[i][j], end=' ')
        print("")