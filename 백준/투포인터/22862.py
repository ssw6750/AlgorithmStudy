# 87%....

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
r, l = 0, 0
c = 0
mx = 0

while True:
    if r == N:
        mx = max(mx, r-l-c-1)
        break
    if arr[r] % 2 == 1: # 홀수
        if c<K: # 지울 수 있으면
            c+=1
            r+=1
        else:
            mx = max(mx, r-l-K)
            if arr[l] % 2 == 1:
                c-=1
            l+=1
    else:
        r+=1

print(mx)

