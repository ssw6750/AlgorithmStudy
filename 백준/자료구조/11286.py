import sys
from queue import PriorityQueue

que = PriorityQueue()

N = int(sys.stdin.readline())
arr=[]
for i in range(N):
    tmp = int(sys.stdin.readline())
    if tmp != 0:
        if tmp<=0:
            que.put((tmp*(-2)-1, tmp))
        else:
            que.put((tmp*2, tmp))
    else:
        if que.qsize()==0:
            print(0)
        else:
            print(que.get()[1])
