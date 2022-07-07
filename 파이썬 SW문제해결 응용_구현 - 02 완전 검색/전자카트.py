def F(x, k):
    print('k=',k)
    print(ar)
    print(N)
    global r
    if x in ar:
        ar.remove(x)
        print(ar)
    else: return

    if len(ar) == 0:
        if r > k:
            r = k
    for i in range(N):
        if i == x: continue
        print(arr[x][i])
        F(i, k+arr[x][i])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    r = 99999999
    arr = []
    ar = []

    N = int(input())
    for i in range(0, N):
        arr.append(list(map(int, input().split())))

    for j in range(N):
        ar.append(j)

    F(0, 0)

    print("#{} {}".format(test_case, r))