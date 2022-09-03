import sys
input = sys.stdin.readline

n = int(input())
ar = list(map(int, input().split()))
ar.sort()
mx = 0
if n%2 == 1:
    mx = ar.pop()
    n= n-1

for i in range(n//2):
    mx = max(ar[i]+ar[n-1-i], mx)

print(mx)
