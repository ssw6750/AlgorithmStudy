T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))
    que = []

    for i in range(N):
        que.append([que[i], i])

    i = 0

    while len(que)!=1:
        que[0][0] //= 2

        if que[0][0] == 0:
            if N+ i < M:
                que.pop(0)
                que.append([l[N+i], N+i])
                i+=1
            elif N+i >= M:
                que.pop(0)
        else:
            que.append(que.pop(0))


    print('#{} {}'.format(test_case, que[0][1]+1))