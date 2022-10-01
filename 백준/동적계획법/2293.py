from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
ar = []
dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    ar.append(int(input()))


for i in ar:
    for j in range(i, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])


