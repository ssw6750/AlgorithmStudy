import sys
input = sys.stdin.readline

n = int(input())
ar = [0, 0, 1, 1]
d = ar + [0] * (n - 3)

for i in range(4, n + 1):
    mn = d[i-1]
    if i%3 == 0:
        mn = min(d[i//3], mn)
    if i%2 == 0:
        mn = min(d[i//2], mn)
    d[i] = mn + 1

print(d[n])

