import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a>b:
        parent[a] = b
        s[b] += s[a]
        s[a] = 0
    elif a<b:
        parent[b] = a
        s[a] += s[b]
        s[b] = 0

def Find(u):
    if parent[u]==u:
        return u
    parent[u] = Find(parent[u])
    return parent[u]

parent = [i for i in range(10**6 + 1)]
s = [1 for i in range(10**6 + 1)]
n = int(input())

for i in range(n):
    tmp = list(map(str, input().split()))
    if tmp[0] == 'I':
        Union(int(tmp[1]), int(tmp[2]))
    else: print(s[Find(int(tmp[1]))])
