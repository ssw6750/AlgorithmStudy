#테케만 맞음...

import sys
input = sys.stdin.readline

def d_max(a, b):
    global f
    if a > b:
        return a, 0
    else:
        return b, 1

for _ in range(int(input())):
    f = 0
    n = int(input())
    ar = []
    for _ in range(2):
        ar.append([0] + list(map(int, input().split())))

    dp = [[0,-1] for _ in range(n+1)]
    dp[1][0], dp[1][1] = d_max(ar[0][1], ar[1][1])

    for i in range(2, n+1):
        v, f = dp[i-1][0], dp[i-1][1]
        if f == 0:
            tmp = v+ar[1][i]
            ff = 1
        else:
            tmp = v+ar[0][i]
            ff = 0

        v2, f2 = d_max(ar[0][i], ar[1][i])

        if dp[i-2][0]+v2 > tmp:
            dp[i][0], dp[i][1]=dp[i-2][0]+v2, f2
        else: dp[i][0], dp[i][1] = tmp, ff

    print(dp[n][0])

