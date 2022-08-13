import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mx = []
arr = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    mx.append(list(map(int, input().split())))
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = mx[i-1][j-1]+arr[i][j-1]+arr[i-1][j]-arr[i-1][j-1]
k = int(input())
for i in range(k):
    i, j, x, y = map(int, input().split())
    print(arr[x][y] - arr[x][j-1] - arr[i-1][y] + arr[i-1][j-1])