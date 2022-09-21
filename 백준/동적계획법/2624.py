# 점화식 dp[i][j] = dp[i][j] + dp[i-1][j-v*val] ( 1 <= v <= c)

import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
ar = [[0,0]]
for i in range(k):
    ar.append(list(map(int, input().split())))

dp=[[0] * (t+1) for _ in range(k+1)]
dp[0][0] = 1

for i in range(1, k+1):
    v, c = ar[i]
    for j in range(t+1):
        dp[i][j] = dp[i-1][j]
        for o in range(1, c+1):
            if j-v*o >= 0:
                dp[i][j] += dp[i-1][j-v*o]
            else:
                break

print(dp[k][t])