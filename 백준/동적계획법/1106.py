# 인원수가 넘어갔을때 최소비용이 나오는 경우 고려

from sys import stdin
input = stdin.readline

c, n = map(int, input().split())
ar = []

dp = [99999] * (c+100)
dp  [0] = 0
for i in range(n):
    ar.append(list(map(int, input().split())))

ar1 = sorted(ar, key= lambda x: x[0])

for i in ar1:
    cost, cnt = i[0], i[1]
    for j in range(cnt, c+100):
        dp[j] = min(dp[j-cnt]+cost, dp[j])

print(min(dp[c:]))