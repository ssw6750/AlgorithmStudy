import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def F(x, cnt):
    v[x] = cnt
    if x*2<100001 and v[x*2] == -1:
        F(x*2, cnt)
    if x+1<100001 and v[x+1] == -1:
        F(x+1, cnt+1)
    if x-1<100001 and v[x-1] == -1:
        F(x-1, cnt+1)

n,k = map(int,input().split())
v = [-1] * 100001

F(n, 0)

print(v[k])