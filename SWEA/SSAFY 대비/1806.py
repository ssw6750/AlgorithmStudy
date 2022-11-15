import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

mn =  100000001
l, r = 0, 0
sum = 0

while True:
   if sum >= s:
       mn = min(mn, r - l)
       sum -= arr[l]
       l += 1

   elif r == n:
       break

   else:
       sum += arr[r]
       r += 1

if mn == 100000001:
   print(0)
else:
   print(mn)
