# https://velog.io/@jinho0705/SWEA-4871.-%EA%B7%B8%EB%9E%98%ED%94%84-%EA%B2%BD%EB%A1%9Cpython

#테스트 케이스 수 입력
T = int(input())
for test_case in range(1, T+1):
    #정점과 간선의 개수 입력
    N, K = map(int,input().split())
    arr = [[0] *(N+1) for _ in range(N+1)]
    #arr에 입력받은 연결된 정점 표시
    for _ in range(K):
        x, y = map(int,input().split())
        arr[x][y] = 1
    result = 1
    #입력받은 a가 b에 연결되어있는지 확인
    S, G= map(int,input().split())
    if not dfs(S,G):
        result = 0
    print('#{} {}'.format(test_case, result))


def dfs(start, end):
    stack = []
    visit = [False] * (V+1)
    stack.append(start)
    # 입력받은 start부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    while stack:
        v = stack.pop()
        visit[v]=True
        for w in range(V+1):
            if not visit[w]:
                if arr[v][w]:
                    stack.append(w)
    # end 지점을 방문하였는지 반환
    return visit[end]