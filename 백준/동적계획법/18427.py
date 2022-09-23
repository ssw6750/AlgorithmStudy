import sys
input = sys.stdin.readline

def F(idx, h):
    global cnt
    if h == 0:
        cnt+=1
    elif h > 0:
        if idx < n:
            F(idx+1, h)
            for i in ar[idx]:
                F(idx+1, h-i)

n, m, h = map(int, input().split())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))
cnt = 0

F(0, h)
print(cnt)