import sys
input = sys.stdin.readline

n = int(input())
ar = []

mtx = [[0]*1001 for _ in range(1001)]

for i in range(1,n+1):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(x1,x1+x2):
        for k in range(y1,y1+y2):
            mtx[j][k] = i

for i in range(1, n+1):
    ans = 0
    for j in range(1001):
        for k in range(1001):
            if mtx[j][k] == i:
                ans+=1
    print(ans)

