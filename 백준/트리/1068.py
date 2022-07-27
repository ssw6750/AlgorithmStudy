import sys, math
input = sys.stdin.readline

def DFS(k):
    arr[k] = -2
    for i in range(N):
        if arr[i] == k:
            DFS(i)

N = int(input())
arr = list(map(int, input().split()))
K = int(input())
DFS(K)

#리프노드 구하는 방법
count=0
for i in range(N):
    if arr[i] != -2 and i not in arr:
        count+=1

print(count)
