# 83%...

import sys
import copy
input = sys.stdin.readline  

r1 = [1, -1, 0, 0]
c1 = [0, 0, 1, -1]

def F(t):
    while True:
        for i in range(R):
            for j in range(C):
                g[i][j] -= 1
        for i in range(R):
            for j in range(C):
                if g[i][j] <= 0:
                    g[i][j] = 3
        # print(g)
        t-=1
        if t<=0 : break

        for i in range(R):
            for j in range(C):
                g[i][j] -= 1
        temp = copy.deepcopy(g)
        for i in range(R):
            for j in range(C):
                if temp[i][j] <= 0:
                    g[i][j] = 0
                    for k in range(4):
                        nr = i+r1[k]
                        nc = j+c1[k]
                        if (nr >= 0 and nr < R ) and (nc >= 0 and nc < C):
                            g[nr][nc] = 0
        # print(g)
        t-=1
        if t<=0 : break

R, C, N = map(int, input().split())
# arr = list(map(int, input().split()) for _ in range(R))
g = list([0]*C for _ in range(R))

for i in range(R):
    tmp = input()
    for j in range(len(tmp)):
        if tmp[j] == 'O':
            g[i][j] = 2 #터지는 시간 고려

F(N-1)
for i in range(R):
    for j in range(C):
        if g[i][j] != 0:
            print('O', end='')
        else: print('.', end='')
        # print('')
    print('')

