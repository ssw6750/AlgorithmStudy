# 점화식..
# dp[n][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1] + dp[n][k-1] 
# dp[n-1][k] = dp[0][k-1] + dp[1][k-1] + ... dp[n-1][k-1]
# dp[n][k] = dp[n-1][k] + dp[n][k-1]

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
dp = [[0] * (k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)


# import sys
# input = sys.stdin.readline

# def F(n, k):
#     global cnt
#     if k == 1:
#         cnt+=1
#         return
#     for i in range(n+1):
#         F(n-i, k-1)


# n, k = map(int, input().split())
# cnt = 0

# F(n, k)
# print(cnt%1000000000)
