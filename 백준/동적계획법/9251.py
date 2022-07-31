#lcs

import sys
input = sys.stdin.readline

w1, w2 = map(int, input().split())
l1, l2 = len(w1), len(w2)
memo = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < memo[j]:
            cnt = memo[j]
        elif w1[i] == w2[j]:
            memo[j] = cnt + 1
print(max(memo))