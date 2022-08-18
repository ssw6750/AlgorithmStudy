import sys
input = sys.stdin.readline

def Union(a,b):
    a = Find(a)
    b = Find(b)

    if a>b:
        parent[a] = b
    else:
        parent[b] = a

def Find(u):
    if parent[u]==u:
        return u
    parent[u] = Find(parent[u])
    return parent[u]

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

for i in range(1, n+1):
    tmp = [0] + list(map(int, input().split()))
    for j in range(1, n+1):
        if tmp[j] == 1:
            Union(i, j)

c = list(map(int, input().split()))

p = Find(c[0])
f = False
for i in c[1:]:
    if Find(i) != p:
        f=True
        break

print('YES') if f == False else print('NO') 


