# 다시 품

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0]*(M+1)]
for i in range(N):
    arr.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        arr[i][j] = arr[i][j] + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]


K = int(input())
for i in range(K):
    a, b, c, d = map(int, input().split())
    print(arr[c][d]-arr[a-1][d]-arr[c][b-1]+arr[a-1][b-1])

