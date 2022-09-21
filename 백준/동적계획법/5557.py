import sys
input = sys.stdin.readline

n = int(input())
ar = [0] + list(map(int, input().split()))
cnt = 0

d = [0] * 21
d[ar[1]] = 1

for i in range(2, n):
    tmp_ar=[0] * 21
    for j in range(21):
        if d[j] > 0:
            tmp = j+ar[i]
            tmp2 = j-ar[i]
            if (20 >= tmp >= 0): tmp_ar[tmp] +=d[j]
            if (20 >= tmp2 >= 0): tmp_ar[tmp2] +=d[j]
    d= tmp_ar

print(d[ar[n]])



# import sys
# input = sys.stdin.readline

# n = int(input())
# ar = [0] + list(map(int, input().split()))
# cnt = 0

# d = [[] for _ in range(n+1)]
# d[1].append(ar[1])

# for i in range(2, n):
#     for j in range(len(d[i-1])):
#         tmp = d[i-1][j] + ar[i]
#         tmp2 = d[i-1][j] - ar[i]
#         if (20 >= tmp >= 0): d[i].append(tmp)
#         if (20 >= tmp2 >= 0): d[i].append(tmp2)

# for i in d[n-1]:
#     if i == ar[n]:
#         cnt +=1
# print(cnt)
