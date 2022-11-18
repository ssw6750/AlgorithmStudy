import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
ar = []
ans = 0
for i in range(k):
    ar.append(list(map(int, input().split())))

for i in range(k):
    for j in range(k):
        cnt=0
        x = ar[i][0]
        y = ar[j][1]

        for o in range(k):
            nx = ar[o][0]
            ny = ar[o][1]
            if x <= nx <= x+l and y <= ny <= y+l:
                cnt+=1
        ans = max(ans, cnt)

print(k - ans)   
