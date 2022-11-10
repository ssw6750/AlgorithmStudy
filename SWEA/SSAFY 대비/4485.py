# 힙큐 사용..

from heapq import heappush, heappop
import sys

INF = sys.maxsize
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


t = 1

while True:
    n = int(input())
    if n == 0:
        break

    mtx = []
    for i in range(n):
        mtx.append(list(map(int, input().split())))

    dist = [[INF]*n for _ in range(n)]
    q = []
    heappush(q, [mtx[0][0], 0, 0])
    dist[0][0] = 0
    while q:
        w, x, y = heappop(q)
        if x == n-1 and y == n-1:
            print("Problem {0}: {1}".format(t, w))
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                nw = w + mtx[nx][ny]
                if nw < dist[nx][ny]: # 작은것
                    dist[nx][ny] = nw
                    heappush(q, [nw, nx, ny])
    t += 1