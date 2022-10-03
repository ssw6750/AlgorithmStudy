from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
ar = []
dp = [99999] * (k+1)
dp[0] = 0
for i in range(n):
    ar.append(int(input()))


for i in ar:
    for j in range(i, k+1):
        dp[j] = min(dp[j-i] + 1,dp[j])

if dp[k] == 99999:
    print(-1)
else:
    print(dp[k])