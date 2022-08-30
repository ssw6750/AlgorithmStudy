import heapq
import sys
input = sys.stdin.readline

for t in range(int(input())):
    k = int(input())
    heap1 = []
    heap2 = []

    exist = [False] * k

    for i in range(k):
        c, n = map(str, input().split())
        if c == 'I':
            heapq.heappush(heap1, (int(n), i))
            heapq.heappush(heap2, (-(int(n)), i))
            exist[i] = True
        else:
            if len(heap1) == 0:
                continue
            if n == '1':
                while heap2 and not exist[heap2[0][1]]:
                    heapq.heappop(heap2)
                if heap2:
                    exist[heap2[0][1]] = False
                    heapq.heappop(heap2)
            else:
                while heap1 and not exist[heap1[0][1]]:
                    heapq.heappop(heap1)
                if heap1:
                    exist[heap1[0][1]] = False
                    heapq.heappop(heap1)

    while heap2 and not exist[heap2[0][1]]:
                    heapq.heappop(heap2)
    while heap1 and not exist[heap1[0][1]]:
                    heapq.heappop(heap1)

    if heap1:
        print(("{} {}").format(-heapq.heappop(heap2)[0], heapq.heappop(heap1)[0])) 
    else:
        print("EMPTY")
                