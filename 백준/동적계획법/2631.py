# 최대증가 부분수열 LIS

import sys
input = sys.stdin.readline

n = int(input())
ar = []
for i in range(n):
    ar.append(int(input()))

d=[0 for _ in range(n)]
d[0]=1
mx=0
for i in range(1,n):
   for j in range(0,i):
      if ar[i] > ar[j]:
         mx = max(mx,d[j])
   d[i]=mx+1
   print(d)
   mx=0

print(n-max(d)) 