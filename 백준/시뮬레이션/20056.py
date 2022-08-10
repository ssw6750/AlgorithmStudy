import sys
from collections import deque
input = sys.stdin.readline  

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M, K = map(int, input().split())
arr = deque()
for i in range(M):
    r, c, m, s, d = list(map(int, input().split()))
    arr.append([r-1, c-1, m, s, d])

mx = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    while arr:
        r, c, m, s, d = arr.popleft()
        nr = (r + s * dx[d]) % N  
        nc = (c + s * dy[d]) % N
        mx[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(mx[i][j]) > 1:
                sm = 0
                ss = 0
                odd = 0
                even = 0
                c = len(mx[i][j]) 
                while mx[i][j]:
                    m, s, d = mx[i][j].pop(0)
                    sm += m
                    ss += s
                    if d % 2 == 1:
                        odd += 1
                    else:
                        even += 1
                if odd == c or even == c: 
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sm//5 > 0: 
                    for k in nd:
                        arr.append([i, j, sm//5, ss//c, k])

            if len(mx[i][j]) == 1:
                arr.append([i, j] + mx[i][j].pop())

sum = 0
for i in arr:
    sum+=i[2]

print(sum)