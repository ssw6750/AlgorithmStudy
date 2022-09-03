import sys
input = sys.stdin.readline

ar = []
n = int(input())
for i in range(n):
    ar.append(int(input()))
ar.sort()
tmp = 0
for i in range(len(ar)-3,-1,-3):
    tmp += ar[i]

print(sum(ar)-tmp)