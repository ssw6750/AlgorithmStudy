# 냅색 알고리즘

import sys
input = sys.stdin.readline   

N, K = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
memo = knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(0, N):
    for j in range(1, K+1):
        w = arr[i][0]
        v = arr[i][1]
        if j < w : memo[i+1][j] = memo[i][j]
        else: memo[i+1][j] = max(v+memo[i][j-w], memo[i][j])

print(memo[N][K])

# import sys
# input = sys.stdin.readline

# n,k = map(int,input().split())
# bag = [0] * (k+1)
    
# for _ in range(n):
#     w,v = map(int,input().split())
#     for i in range(k,w-1,-1):
#         pre_v = bag[i]       # 가방에 현재 물건 X
#         now_v = v + bag[i-w] # 가방에 현재 물건 O
#         bag[i] = max(pre_v,now_v)
# print(bag[k]) # 가방무게가 k일 때 물건 최대 가치