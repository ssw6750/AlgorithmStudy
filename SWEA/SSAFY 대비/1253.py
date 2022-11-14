import sys
input = sys.stdin.readline

n = int(input())
ar = sorted(map(int, input().split()))

answer = 0

for i in range(n):
    k = ar[i]
    tmp = ar[:i] + ar[i+1:]
    start, end = 0, len(tmp) - 1

    while start < end:
        s =  tmp[start] + tmp[end]
        if k == s:
            answer += 1
            break
        elif k > s:
            start += 1
        elif k < s:
            end -= 1

print(answer)

# 시간 초과
# n = int(input())
# ar = list(map(int, input().split()))

# ans = 0
# for i in range(n):
#     k = ar[i]
#     tmp = ar[:i]+ar[i+1:]
#     f = False

#     for j in range(n-1):
#         n1 = tmp[j]
#         for s in range(n-1):
#             if s == j: continue
#             n2 = tmp[s]
#             if n1 + n2 == k:
#                 ans+=1
#                 f=True
#                 break
#         if f: break

# print(ans)