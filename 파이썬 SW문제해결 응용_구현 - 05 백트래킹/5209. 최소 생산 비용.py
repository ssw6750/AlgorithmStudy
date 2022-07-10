def F(idx, cnt, visited):
    global min 
    if cnt >= min:
        return
    if idx > N-1:
        if min > cnt:
            min = cnt
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i]=1
            F(idx+1, cnt+M[idx][i], visited)
            visited[i]=0
        


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    M = []
    N = int(input())
    for i in range(N):
        M.append(list(map(int, input().split())))
    min = 9999999
    visited = [0]*N
    F(0, 0, visited)
    print("#{} {}".format(test_case, min, visited))

