import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
km = list(map(int, input().split()))
p = list(map(int, input().split()))
s = 0
min = 1000000000

for i in range(len(km)):
    if p[i] < min:
        min = p[i]
    s += min*km[i]

print(s)



