import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()
arr.reverse()
s=0

for i in range(len(arr)):
    if arr[i]-(i) > 0:
        s+=arr[i]-(i)
    

print(s)