import sys
input = sys.stdin.readline

n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        dy = i+ar[i][j]
        dx = j+ar[i][j]

        if dy < n:
            dp[dy][j] += dp[i][j]
        if dx < n:
            dp[i][dx] += dp[i][j]

print(dp[n-1][n-1])

