def F(idx, cnt):
    global min 
    cnt+=1
    if cnt >= min:
        return
    tmp = cnt
    for i in range(M[idx]):
        if idx+1+i < N-1:
            F(idx+1+i, tmp)
        else:
            if tmp < min:
                min = tmp


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N, *arr = map(int, input().split())
    A = list(map(int, input().split()))
    N = A[0]
    M = A[1:]
    min = 9999999
    F(0, 0)

    print("#{} {}".format(test_case, min-1))

