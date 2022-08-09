import sys
input = sys.stdin.readline  

n = int(input())
ar1 = list(map(int, input().split()))
m = int(input())
ar2 = list(map(int, input().split()))
ans = []
ar1.sort()

for i in range(m):
    s = 0
    e = n-1
    f=False
    while(s<=e):
        mid = (s+e)//2
        if ar2[i] > ar1[mid]:
            s = mid + 1
        elif ar2[i] < ar1[mid]:
            e = mid -1
        elif ar2[i] == ar1[mid]:
            ans.append(1)
            f = True
            break
    if f==False: ans.append(0)

print(str(ans)[1:-1].replace(',',''))