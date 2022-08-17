from array import array
import sys
import collections

input = sys.stdin.readline
N, M = map(int, input().split())
inDegree = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
graph = collections.defaultdict(list)

for i in range(M):
    tmp = list(map(int, input().split()))
    for j in range(1,len(tmp)-1):
        graph[tmp[j]].append(tmp[j+1])
        inDegree[tmp[j+1]]+=1

queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = 1

ar = []

while queue:
    node = queue.popleft()
    ar.append(node)
    for i in graph[node]:
        inDegree[i] -= 1
        dp[i] = max(dp[node] + 1, dp[i])
        if inDegree[i] == 0:
            queue.append(i)

if sum(inDegree) != 0:
    print(0)
else:
    for i in ar:
        print(i)