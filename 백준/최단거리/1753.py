import sys, heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF: print('INF')
    else: print(distance[i])