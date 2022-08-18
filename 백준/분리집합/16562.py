import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a>b:
        parent[a] = b
        if s[a] < s[b]:
            s[b] = s[a]
            s[a] = 0
        else: s[a] = 0
    else:
        parent[b] = a
        if s[a] > s[b]:
            s[a] = s[b]
            s[b] = 0
        else: s[b] = 0

def Find(u):
    if parent[u]==u:
        return u
    parent[u] = Find(parent[u])
    return parent[u]

n,m,k = map(int,input().split())
parent = [i for i in range(n+1)]
s = [0] + list(map(int,input().split()))

for _ in range(m):
    v, w = map(int,input().split())
    Union(v, w)

print(sum(s)) if sum(s) <= k else print("Oh no")