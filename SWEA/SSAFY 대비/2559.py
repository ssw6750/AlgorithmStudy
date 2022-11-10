# 시간 초과 주의!!

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ar = list(map(int, input().split()))
ans = []
ans.append(sum(ar[:k]))

for i in range(n - k):
    ans.append(ans[i] - ar[i] + ar[k+i])

print(max(ans))