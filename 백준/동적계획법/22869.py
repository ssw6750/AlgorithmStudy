import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
dp = [0] * n
f = True
q = deque([0])
dp[0] = 1
while q:
    i = q.popleft()
    for j in range(i + 1, n):
        if (j - i) * (1 + abs(s[i] - s[j])) <= k:
            if not dp[j]:
                dp[j] = 1
                q.append(j)
                if j == n - 1:
                    print('YES')
                    f = False
                    break
if f:
    print('NO')