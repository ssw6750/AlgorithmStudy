def F(x, y, k):
    global r
    if x > N-1 or y > N-1:
        return
    if x == N-1 and y == N-1:
        if k+arr[x][y] < r:
            r = k+arr[x][y]
    if k+arr[x][y] > r:
        return

    k = k+arr[x][y]

    for d in range(2):
        x1 = x+dx[d]
        y1 = y+dy[d]
        F(x1, y1, k)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    r = 99999999
    arr = []
    dx = [0, 1]
    dy = [1, 0]

    N = int(input())
    for i in range(0, N):
        arr.append(list(map(int, input().split())))

    F(0, 0, 0)

    print("#{} {}".format(test_case, r))



    