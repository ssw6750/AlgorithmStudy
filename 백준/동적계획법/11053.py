import sys
input = sys.stdin.readline

n = int(input())
ar = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if ar[i] > ar[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))