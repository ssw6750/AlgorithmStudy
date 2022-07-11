def binarySearch(arr, t, l, r):
    if l > r:
        return
    global Lflag
    global Rflag
    global cnt
    m = (l+r)//2
    middle = arr[m]
    if t == middle:
        cnt +=1
    elif middle > t:
        if Lflag == True:
            return
        else:
            Lflag = True
            Rflag = False
            binarySearch(arr, t, l, m-1)
    elif middle < t:
        if Rflag == True:
            return
        else:
            Rflag = True
            Lflag = False
            binarySearch(arr, t, m+1, r)
    else: 
        Lflag = False
        Rflag = False
        return

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0

    for i in range(M):
        Lflag = False
        Rflag = False
        binarySearch(A, B[i], 0, N-1)

    print("#{} {}".format(test_case, cnt))
