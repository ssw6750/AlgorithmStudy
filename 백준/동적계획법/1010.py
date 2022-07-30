import sys
input = sys.stdin.readline

def F(a, b):
    global c
    if a == 1:
        c+=b
    else:
        for i in range(1,b-a+1):
            F(a-1, b-i)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    c = 0

