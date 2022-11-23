import sys
input = sys.stdin.readline

n, k = map(int, input().split())
f = [0] * 7
m = [0] * 7

for i in range(n):
    s, y = map(int, input().split())
    if s == 0:
        f[y] += 1
    else: 
        m[y] += 1

ans = 0
for i in range(1, 7):
    a, b = divmod(f[i], k)
    if b == 0:
        ans+=a
    else :
        ans+=a+1

    a, b = divmod(m[i], k)
    if b == 0:
        ans+=a
    else :
        ans+=a+1

print(ans)