import sys
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

r, c = map(int, input().split())
mtx = [list(input()) for _ in range(r)]
v = [[0]*c for _ in range(r)]
vv = set()
ans = 0


def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    vv.add(mtx[y][x])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r:
            if mtx[ny][nx] not in vv:
                dfs(nx, ny, cnt + 1)

    vv.remove(mtx[y][x])

dfs(0, 0, 1)

print(ans)