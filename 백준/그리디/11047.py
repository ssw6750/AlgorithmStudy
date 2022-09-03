import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ar = []
for i in range(n):
    ar.append(int(input()))

idx = n-1
cnt = 0
while True:
    if k <= 0: break
    if k < ar[idx]:
        idx-=1
    else:
        k -= ar[idx]
        cnt+=1

print(cnt)
