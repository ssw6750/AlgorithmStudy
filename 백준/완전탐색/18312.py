# 09시

import sys
input = sys.stdin.readline  

n, K = map(int, input().split())
K = str(K)
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if K in str(i) or K in str(j) or K in str(k):
                cnt+=1 

print(cnt)