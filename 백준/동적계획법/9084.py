import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    sum=0
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    memo = [0]*(M+1)
    memo[0] = 1

    for i in arr:
        for j in range(1, M+1):
            if j - i >= 0:
                memo[j]+=memo[j-i]

    print(memo[M])