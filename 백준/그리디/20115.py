import sys
input = sys.stdin.readline

n = int(input())
ar = list(map(int, input().split()))
ar.sort()
for i in range(n-1):
    ar[-1] = ar[-1] + ar[i]/2

print(ar[-1])