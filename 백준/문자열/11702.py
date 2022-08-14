import sys
input = sys.stdin.readline

n = int(input())
ar = list(input())
sum = 0
for i in range(n):
    sum+=int(ar[i])

print(sum)
    