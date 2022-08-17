import sys
import collections

input = sys.stdin.readline

N = int(input())
inDegree = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
graph = collections.defaultdict(list)
ar = [0 for _ in range(N + 1)]

for i in range(1,N+1):
    tmp = list(map(int, input().split()))
    ar[i] += tmp[0]
    for j in range(tmp[1]):
        graph[tmp[2+j]].append(i)
        inDegree[i] += 1


queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = ar[i]

while queue:
    node = queue.popleft()
    for i in graph[node]:
        inDegree[i] -= 1
        dp[i] = max(dp[node] + ar[i], dp[i])
        if inDegree[i] == 0:
            queue.append(i)

print(max(dp))