T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    def f(y, x, cnt, ar):
        global k
        cnt+=1
        arr[y][x] = -1
        if k == 1:
            return
        for i in range(0, 4):
            y2 = y + dy[i]
            x2 = x + dx[i]
            if arr[y2][x2] == 3:
                ar.append(cnt)
                k = 1
                return
            if arr[y2][x2] == 0:
                f(y2, x2, cnt, ar)
    arr=[]
    ar=[]
    start = []
    k = 0
    N = int(input())
    arr.append([1]*(N+2))
    for i in range(0,N):
        l = list(map(int, str(input())))
        l.append(1)
        l.insert(0, 1)
        arr.append(l)   #숫자를 리스트 변환
    arr.append([1]*(N+2))

    for i in range (0, N+2):
        for j in range (0, N+2):
            if arr[i][j] == 2:
                start.append(i)
                start.append(j)
                
    f(start[0], start[1], 0, ar)

    if k == 1:
        k = min(ar)-1

    print("#{} {}".format(test_case, k))