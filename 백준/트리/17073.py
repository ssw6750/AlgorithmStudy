import sys, math
input = sys.stdin.readline

n, w = map(int, input().split())
g = [[] for _ in range(n+1)]
while True:
    try:
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    except:
        break
count=0
for i in range(1,n+1):
    if len(g[i]) <= 1 and i!=1:
        count+=1

print("{:.10f}".format(w/count))
