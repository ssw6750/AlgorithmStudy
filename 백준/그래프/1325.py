import sys
input = sys.stdin.readline  
from collections import deque

def BFS(n):
    que = deque([n])
    v = [False]*(N+1)
    v[n] = True
    s = 1
    while que:
        n1 = que.popleft() 
        for i in g[n1]:
            if v[i] == False:
                v[i] = True
                que.append(i)
                s+=1
    return s
    
N, M = map(int, input().split())
g = list([] for _ in range(N+1)) 

for i in range(M):
    a, b = map(int, input().split())
    g[b].append(a)

ans = []
max = 0
for i in range(1,N+1):
    r = BFS(i)
    if r>max:
        max=r
        ans=[i]
    elif r == max:
        ans.append(i)

print(str(ans)[1:-1].replace(',',''))
    