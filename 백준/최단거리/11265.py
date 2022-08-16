# https://www.youtube.com/watch?v=hw-SvAR3Zqg

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N): 
    for i in range(N):
        for j in range(N): 
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(M):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else: print("Stay here")
