from collections import deque

def bfs(i, j):
    distance[i][j] = 0

    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                diff = 0
                if region[nx][ny] > region[x][y]:
                    diff = region[nx][ny] - region[x][y]

                if distance[x][y] + 1 + diff < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] + 1 + diff
                    queue.append((nx, ny))

    return distance[N-1][N-1]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    region = [list(map(int, input().split())) for _ in range(N)]

    distance = [[float('inf') for _ in range(N)] for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    print('#{} {}'.format(test_case, bfs(0, 0)))