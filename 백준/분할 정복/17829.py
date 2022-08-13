import sys
input = sys.stdin.readline

def pooling(size, x, y):
    mid=size//2
    if size==2:
        answer=[mx[x][y], mx[x+1][y], mx[x][y+1], mx[x+1][y+1]]
        answer.sort()
        return answer[-2]
    lt=pooling(mid, x, y)
    rt=pooling(mid, x+mid, y)
    lb=pooling(mid, x, y+mid)
    rb=pooling(mid, x+mid, y+mid)
    answer=[lt, rt, lb, rb]
    answer.sort()
    return answer[-2]

n = int(input())
mx = [list(map(int, input().split)) for _ in range(n)]

print(pooling(n, 0, 0))



