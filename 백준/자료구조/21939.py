import heapq
import sys
input = sys.stdin.readline

q1 = []
q2 = []
exist = [False] * 11000

n = int(input())
for i in range(n):
    p, l = map(int, input().split())
    heapq.heappush(q1, (l, p, i))
    heapq.heappush(q2, (-l, -p, i))
    exist[i] = True

m = int(input())
for i in range(m):
    tmp = input().split()
    if tmp[0] == "add":
        p = int(tmp[1])
        l = int(tmp[2])
        heapq.heappush(q1, (l, p, n+i))
        heapq.heappush(q2, (-l, -p, n+i))
        exist[n+i] = True
    elif tmp[0] == "solved":
        for j in q1:
            if j[1] == int(tmp[1]):
                exist[j[2]] = False 
    elif tmp[0] == "recommend":
        if tmp[1] == '1':
            while q2 and not exist[q2[0][2]]:
                heapq.heappop(q2)
            if q2:
                exist[q2[0][2]] = False
                print(-heapq.heappop(q2)[1])
        else:
            while q1 and not exist[q1[0][2]]:
                heapq.heappop(q1)
            if q1:
                exist[q1[0][2]] = False
                print(heapq.heappop(q1)[1])




