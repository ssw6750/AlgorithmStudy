# 1퍼에서 멈춤..ㅜ
# 그리디로 풀어서 틀린듯 확실하지 않음
# 다시 풀기

# from sys import stdin
# input = stdin.readline

# def dp(idx, d, f):
#     v[idx] = min(v[idx], d)
#     if f == False and idx + 3 <n:
#         dp(idx+3, v[idx]+k, True)
#     if idx + 2<n:
#         dp(idx+2, v[idx]+ar[idx][1], f)
#     if idx + 1<n:
#         dp(idx+1, v[idx]+ar[idx][0], f)


# n = int(input())
# ar = []
# for i in range(n-1):
#     ar.append(list(map(int, input().split())))
# k = int(input())

# v = [1e9] * n


# if n == 1:
#     print(0)
#     exit()

# dp(0, 0, False)
# print(v[n-1])

# sys.stdin = open("sample_input.txt", "r")





# 서영스 코드 수정
from sys import stdin
input = stdin.readline

SMALL = 0
BIG = 1
INF = (1e9)

n = int(input())
jump = [(INF,INF)] + [tuple(map(int,input().split())) for _ in range(n-1)] # 1돌부터 n-1돌 점프 
k = int(input())

if n == 1:
    print(0)
    exit()
    
dp = [0] + [0] + [jump[1][0]] + [INF] * (n-2) # 0돌부터 n돌까지 거리

# 작은 점프, 큰 점프로만 dp 구하기 
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + jump[i - 1][SMALL], dp[i - 2] + jump[i - 2][BIG])

# 매우 큰 점프 적용해보기
mn = dp[-1] # !!!!!! 변수명에 max, min x
for j in range(1,n-2):
    dp2 = dp[:]
    if dp2[j] + k < dp2[j + 3]:
        dp2[j + 3] = dp2[j] + k
        for i in range(j + 4, n+1): # !!!!! n이 아니라 n+1  ^ㅁ^;;
           dp2[i] = min(dp2[i - 1] + jump[i - 1][SMALL], dp2[i - 2] + jump[i - 2][BIG])
        if mn > dp2[-1]:
            mn = dp2[-1]
print(mn)