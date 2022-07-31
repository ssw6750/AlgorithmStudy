# 시간 초과....

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def F(c, d):
    global a
    global b
    if c<a or d<b: return 0
    if memo[c][d] != 0:
        return memo[c][d]
    F(c-1,d-1)
    F(c-1,d)
    F(c,d-1)
    memo[c][d] = arr[c-1][d-1]+memo[c-1][d]+memo[c][d-1]-memo[c-1][d-1]
    # print(memo[c-1][d-1], arr[c-1][d-1], memo[c-2][d-1], memo[c-1][d-2], memo[c-2][d-2])

N, M = map(int, input().split())
arr = []
arr1 = []
for i in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())

for i in range(K):
    memo = [[0]*(N+1) for _ in range(M+1)]
    a, b, c, d = map(int, input().split())
    sum=0
    F(c, d)
    print(memo[c][d])
