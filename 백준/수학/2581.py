import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
ans1 = 0
ans2 = 0
for i in range(a, b+1):
    if i == 1: continue
    f=False
    for j in range(2,i):
        if i%j == 0:
            f=True
            break
    if f==True:
        continue
    ans1 +=i
    if ans2 == 0:
        ans2 = i

if ans1 > 0:
    print(ans1)
    print(ans2)
else:
    print(-1)