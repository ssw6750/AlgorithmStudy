# import sys

# N = int(sys.stdin.readline())
# tree = {1:0}
# for i in range(N-1):
#     n1, n2 = map(int, sys.stdin.readline().split())
#     if n1 in tree:
#         tree[n2]=n1
#     else:
#         tree[n1]=n2
# keys = list(tree.keys())
# keys.sort()

# for i in keys[1:]:
#     print(tree[i])

import sys

def dfs(s):
    for i in g[s]:
        if v[i] == 0:
            v[i] = s
            dfs(i)

input = sys.stdin.readline

n = int(input())
g = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

v = [0]*(n+1)
arr = []
dfs(1)

for x in range(2, n+1):
    print(v[x])