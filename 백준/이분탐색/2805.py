import sys
input = sys.stdin.readline 

n, m = map(int, input().split())
ar = list(map(int, input().split()))

s=1
e=max(ar)
while s<=e:
    mid=(s+e)//2
    k = 0
    for i in ar:
        if i >= mid:
            k+=i-mid
    if m>k:
        e = mid-1
    else:
        s = mid+1
print(e)