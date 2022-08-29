import sys
input = sys.stdin.readline
from collections import deque

for T in range(int(input())):
    n, m = map(int, input().split())
    ar = deque(list(map(int, input().split())))
    tmp = [0 for _ in range(n)]
    tmp[m] = 1
    cnt = 0

    while True:
        a = ar[0]
        t = tmp[0]
        if a == max(ar):
            cnt+=1
            if t == 1:
                break
            else:
                del ar[0]
                del tmp[0]
        else:
            ar.append(ar[0])
            del ar[0]
            tmp.append(tmp[0])
            del tmp[0]
            
    print(cnt)