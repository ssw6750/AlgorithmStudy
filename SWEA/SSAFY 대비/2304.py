import sys

input = sys.stdin.readline

n = int(input())
ar = []
for i in range(n):
    ar.append(list(map(int, input().split())))

ar.sort()
tmp =[]
ans = 0

mx_h = 0
for i in ar:
    if i[1] > mx_h:
        mx_h = i[1]


s = ar[0]
for i in range(len(ar)):
    if s[1] < ar[i][1]:
        ans+= (ar[i][0]-s[0])*s[1]
        s = ar[i]
    if s[1] == mx_h:
        tmp.append(s[0])
        break


s = ar[-1]
for i in range(len(ar)-1, -1, -1):
    if s[1] < ar[i][1]:
        ans+= (s[0]-ar[i][0])*s[1]
        s = ar[i]
    if s[1] == mx_h:
        tmp.append(s[0])
        break

ans+=mx_h*(tmp[1]-tmp[0]+1)

print(ans)