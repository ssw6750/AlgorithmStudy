# ...

import sys, math
input = sys.stdin.readline

K = int(input())
n = int(math.pow(2,K))
arr=list(map(int, input().split()))
dic = {arr[n//2-1]: n//2-1}
ans=[dic]
p=n//2
ans2 = [list(dic.keys())]

for i in range(K-1):
    tmp={}
    p = p//2
    for a in ans[i].values():
        tmp[arr[a-p]]=a-p
        tmp[arr[a+p]]=a+p
    ans.append(tmp)
    ans2.append(list(tmp.keys()))

for i in ans2:
    print(str(i)[1:-1].replace(",",""))