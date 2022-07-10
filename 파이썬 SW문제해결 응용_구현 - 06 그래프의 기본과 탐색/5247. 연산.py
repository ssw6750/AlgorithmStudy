#런타임에러

from collections import deque

def bfs(n, cnt):
    k = 0
    deq = deque()
    deq.append([n, cnt])
    while deq:
        v = deq.popleft()
        n = v[0]
        cnt = v[1]
        if n==M:
            k=cnt
            break
        if n>=1000000 or n<=0:
            continue
        if visited[n] == 0:
            visited[n]=1
            deq.append([n+1,cnt+1])
            deq.append([n-1,cnt+1])
            deq.append([n*2,cnt+1])
            deq.append([n-10,cnt+1])

    return k


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0]*1000000 # 중요
    print("#{} {}".format(test_case, bfs(N, 0)))