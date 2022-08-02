import sys
# from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
r, l = 0, 0
cnt = [0] * (max(arr) + 1)
ans = 0

while r < N:
    if cnt[arr[r]] < K:
        cnt[arr[r]] += 1
        r += 1
    else:
        cnt[arr[l]] -= 1
        l += 1
    ans = max(ans, r - l)

print(ans)