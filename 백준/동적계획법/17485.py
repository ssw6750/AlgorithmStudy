import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def F(idx, l, v, before):
    global mn
    if v > mn:
        return
    if idx == n:
        if v < mn:
            mn = v
    elif idx==0:
        for i in range(m):
            F(idx+1, i, v+ar[idx][i], 0)
    else:
        if before != 1 and l-1 >= 0:
            F(idx+1, l-1, v+ar[idx][l-1], 1) 
        if before != 2:
            F(idx+1, l, v+ar[idx][l], 2) 
        if before != 3 and l+1 < m:
            F(idx+1, l+1, v+ar[idx][l+1], 3) 


n, m = map(int, input().split())
ar = []
mn = 100*n
for i in range(n):
    ar.append(list(map(int, input().split())))

F(0, 0, 0, 0)

print(mn)