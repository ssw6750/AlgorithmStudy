# 1퍼에서 멈춤..ㅜ
from sys import stdin
input = stdin.readline

def dp(idx, d, f):
    v[idx] = min(v[idx], d)
    if idx + 1<n:
        dp(idx+1, v[idx]+ar[idx][0], f)
    if idx + 2<n:
        dp(idx+2, v[idx]+ar[idx][1], f)
    if f == False and idx + 3 <n:
        dp(idx+3, v[idx]+k, True)


n = int(input())
ar = []
for i in range(n-1):
    ar.append(list(map(int, input().split())))
k = int(input())

v = [9999999] * n
f = False

if n == 1:
    print(0)
    exit()

dp(0, 0, False)
print(v[n-1])