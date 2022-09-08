import sys, heapq
INF = float('inf')

def dijkstra(start, distance, graph):
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

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    tmp1 = graph.copy()
    tmp2 = distance.copy()
    for i in fares:
        graph[i[0]].append((i[1], i[2]))
        graph[i[1]].append((i[0], i[2]))
        
    dijkstra(s, distance, graph)
    mn = distance[a] + distance[b]
    for i in range(1, n+1):
        g = tmp1.copy()
        d = tmp2.copy()
        dijkstra(i, d, g)
        mn = min(distance[i] + d[a] + d[b], mn)
    answer = mn
    return answer