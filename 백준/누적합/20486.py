import sys
from collections import deque
input = sys.stdin.readline

n, k, q, m = map(int, input().split())

k_ar = deque(list(map(int, input().split())))
q_ar = deque(list(map(int, input().split())))
v = deque([1]*(n+3))
que = deque(q_ar)

while que:
    tmp = que.popleft()
    if tmp not in k_ar:
        for i in range(1, ((n + 2) // tmp) + 1):
            if tmp*i not in k_ar:
                v[tmp*i] = 0 

#시간초과
# print(v.count(False)-3)


#누적합 적용
dp_sum = [0] * (n + 3)

for num in range(3, n + 3):
    if num == 3:
        dp_sum[num] = v[num]

    else:
        dp_sum[num] = v[num] + dp_sum[num - 1]


for _ in range(m):
    i, j = map(int, input().split())
    print(dp_sum[j] - dp_sum[i - 1])