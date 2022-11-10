import sys, heapq
input = sys.stdin.readline

n,k = map(int,input().split())
visited = [False]*100001
visited[n] = True
hq = [([0,n])]

while hq:
    t,x = heapq.heappop(hq)
    if x == k:
        print(t)
        break
    dx = x*2
    if dx < len(visited) and not visited[dx]:
        visited[dx] = True
        heapq.heappush(hq,(t,dx))  
    for i in (x+1,x-1):
        if i >= 0 and i < len(visited) and not visited[i]:
            visited[i] = True
            heapq.heappush(hq,(t+1,i))
