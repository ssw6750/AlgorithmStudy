import sys
input = sys.stdin.readline

n = int(input())
ar = list(map(int, input().split()))

dp = [ar[0]]
for i in range(len(ar) - 1):
    dp.append(max(dp[i] + ar[i + 1], ar[i + 1]))

print(max(dp))