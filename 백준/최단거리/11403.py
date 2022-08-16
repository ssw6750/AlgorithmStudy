# https://www.youtube.com/watch?v=hw-SvAR3Zqg

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if i == j: continue
        if graph[i][j] == 0:
            graph[i][j] = 99999 
    
#플로이드 워셜 알고리즘
for k in range(N): 
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
            # graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# for i in range(N):
#     for j in range(N):
#         if i == j: continue
#         if graph[i][j] == 99999:
#             graph[i][j] = 0
#         else : graph[i][j] = 1

for i in graph:
    for j in i:
        print(j, end = " ")
    print()