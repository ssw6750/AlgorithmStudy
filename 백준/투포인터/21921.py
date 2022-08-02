# 투포인터 시간초과
# 주지수랑 비슷?


import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = [0] + list(map(int, input().split()))
ans = []

for i in range(1, N+1):
    arr[i] += arr[i-1]

for i in range(X, N+1):
    sum = arr[i] - arr[i-X]
    ans.append(sum)

max = max(ans)
cnt = ans.count(max)

if max == 0:
    print("SAD")
else:
    print(max)
    print(cnt) 



# max = 0
# cnt = 0

# for i in range(N-X+1):
#     sum = 0
#     for j in range(X):
#         sum+=arr[i+j]
#     if max == sum:
#         cnt +=1
#     elif max < sum:
#         cnt = 1
#         max = sum