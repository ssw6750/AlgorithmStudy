# 시간초과때문에 우선순위 큐사용

import sys
import heapq
input = sys.stdin.readline

n = int(input())
l, r = [], [] 

for i in range(n):
  num = int(input())
  
  if len(l) == len(r):
    heapq.heappush(l, -num)
  else:
    heapq.heappush(r, num)

  if i > 0 and l[0] > r[0]:
    tmp_l = heapq.heappop(l)
    tmp_r = heapq.heappop(r)
    heapq.heappush(l, -tmp_r)
    heapq.heappush(r, -tmp_l)

  print(-l[0])