import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for i in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1


for i in range(1, n):
    for j in range(0, 10):
        if j == 0 and i != 1:
            dp[i+1][j+1] +=dp[i][j] 
        elif j == 9:
            dp[i+1][j-1] +=dp[i][j] 
        else:
            dp[i+1][j-1] +=dp[i][j]
            dp[i+1][j+1] +=dp[i][j]

print(sum(dp[n])%1000000000)