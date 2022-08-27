from sys import stdin

input = stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
edge = []


for i in range(N):
    for j in range(i+1, N):
        edge.append([graph[i][j], i, j])

edge.sort(key=lambda x: x[0])

parent = list(range(N + 1))


def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]


sum = 0
for w, s, e in edge:
    if find(s) != find(e):
        union(s, e)
        sum += w

print(sum)