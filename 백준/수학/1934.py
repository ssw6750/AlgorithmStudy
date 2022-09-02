import math
import sys
input = sys.stdin.readline
for t in range(int(input())):
    a, b = map(int, input().split())

    print(math.lcm(a, b))