# rotate

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
ar = deque(list(map(int, input().split())))
idx = 0
index = [x for x in range(1, n + 1)]

ans = []
# ans.append(ar[idx])
# ar.pop(idx)

while ar:
    idx = ar.popleft()
