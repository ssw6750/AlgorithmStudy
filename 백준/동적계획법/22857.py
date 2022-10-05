# 어렵,.,,

import sys
input = sys.stdin.readline

# n, k = map(int, input().split())
# lst = list(map(int, input().split()))

# cnt = 0
# start, end = 0, 0
# size, size_max = 0, 0
# flag = 1

# for start in range(n):
#     while cnt <= k and flag:
#         if lst[end] % 2:          # 홀수인 경우
#             if cnt == k:
#                 break
#             cnt += 1
#         size += 1
#         if end == n - 1:
#             flag = 0
#             break
#         end += 1
        
#     if size_max < size - cnt:
#         size_max = size - cnt
        
#     if lst[start] % 2:    #홀수인 경우
#         cnt -= 1
        
#     size -= 1

# print(size_max)

# 아이디어 떠올리기가 쉽지 않음...ㅜ
n, k = map(int ,input().split())
s = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
print(dp)

for i in range(1, n + 1):
    s[i] %= 2
    for j in range(k + 1):
        if s[i] == 0: # 짝수
            dp[i][j] = dp[i - 1][j] + 1
        if j != 0 and s[i]: # 홀수
            dp[i][j] = dp[i - 1][j - 1]
        print(dp[i])
    print()
result = []
for i in dp:
    result.append(i[k])
print(max(result))    