# 힙큐
import sys, heapq

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
for _ in range(n-1) :
    for i in list(map(int, sys.stdin.readline().split())):
        print(arr, i)
        if arr[0] < i :
            heapq.heappop(arr)
            heapq.heappush(arr, i)
    
print(arr[0])
