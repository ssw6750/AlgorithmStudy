import heapq
import sys
input = sys.stdin.readline

for t in range(int(input())):
    m = int(input())
    ar = []
    for i in range(m//10+1):
        ar = ar+list(map(int,input().split()))

    print(m//2+1)
    print(ar[0], end=" ")
    if m !=1:
        cnt=1
        for i in range(2,m,2):
            print(sorted(ar[:i+1])[(i+1)//2], end=" ")
            cnt+=1
            if cnt==10:
                print("")
                cnt=0
        else:
            print("")
        