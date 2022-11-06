# 한줄에 20개씩 출력합니다

import sys
input = sys.stdin.readline

def change(idx):
    ar[idx] = 1-ar[idx]

n = int(input())
ar = [0]+list(map(int, input().split()))
c = int(input())
for i in range(c):
    s, a = map(int, input().split())

    if s == 1:
        for k in range(a, n+1, a):
            change(k)
    
    if s == 2:
        change(a)
        ii = 1
        while True:
            if a+ii <=n and a-ii >= 0 and ar[a+ii] == ar[a-ii]:
                change(a+ii)
                change(a-ii)
                ii+=1
            else: break

for i in range(1+n):
    print(ar[i], end =' ')
    if i % 20 == 0:
        print()


