import sys
from collections import deque
input = sys.stdin.readline  

dy = [-1, -1, 0, 0, 1, 1]
dx = [-1, 0, -1, 1, -1, 0]

def F():
    d = 0
    for i in range(n):
        for j in range(m):
            if mt[i][j] == 1

m, n = map(int, input().split())
mt = [list(map(int, input().split())) for _ in range(n)]