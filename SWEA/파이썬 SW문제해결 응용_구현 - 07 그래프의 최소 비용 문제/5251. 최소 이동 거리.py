T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    adj = {i: [] for i in range(N+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    INF = float('inf')
    dist = [INF] * (N+1)
    selected = [0] * (N+1)

    dist[0] = 0
    cnt = 0
    while cnt < (N):
        min = INF
        u = -1
        for i in range(N+1):
            if not selected[i] and dist[i] < min:
                min = dist[i]
                u = i
        # 결정
        selected[u] = True
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:  # 도착정점, 가중치
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost
    print('#{} {}'.format(test_case, dist[N]))