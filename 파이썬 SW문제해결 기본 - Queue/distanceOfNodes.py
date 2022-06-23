# 10개 중 9개, DFS보다 BFS가 더 좋아보임.. BFS공부

def dfs(start, end):
    cnt = 0
    a = False
    arr2 = []
    stack = []
    visit = [False] * (V+1)
    stack.append([start, cnt])
    # 입력받은 start부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    while stack:

        l = stack.pop()
        v = l[0]
        cnt = l[1]+1

        if v == end:
            arr2.append(cnt)
            a = True
        else:
            visit[v]=True

        for w in range(V+1):
            if not visit[w]:
                if arr[v][w] or arr[w][v]:
                    stack.append([w, cnt])

    # end 지점을 방문하였는지 반환
    if not a:
        return 0
    else :
        return min(arr2)-1
#테스트 케이스 수 입력
T = int(input())
for test_case in range(1, T+1):
    #정점과 간선의 개수 입력
    V, E = map(int,input().split())
    arr = [[0] *(V+1) for _ in range(V+1)]
    #arr에 입력받은 연결된 정점 표시
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
    # result = 1
    #입력받은 a가 b에 연결되어있는지 확인
    a, b= map(int,input().split())



    # if not dfs(a,b):
    #     result = 0
    print('#{} {}'.format(test_case, dfs(a,b)))
