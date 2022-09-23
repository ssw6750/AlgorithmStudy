# 점화식 사용

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    arr.append(list(map(int, list(input().rstrip()))))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer * answer)


# 각 좌표마다 나올수 있는 정사각형 크기를 구함
# 시간 초과
# def check(i,j):
#     c = 1
#     while True:
#         tmp = 0
#         if i+c>n: return (c-1)**2
#         if j+c>m: return (c-1)**2
#         for y in range(i, i+c):
#             for x in range(j, j+c):
#                 if mt[y][x] == "0":
#                     return (c-1)**2
#         c+=1

# n, m = map(int, input().split())
# mt = []
# for i in range(n):
#     mt.append(list(input()))

# dp = [] # 시작 좌표와 크기

# for i in range(n):
#     for j in range(m):
#         dp.append(check(i, j))

# print(max(dp))
