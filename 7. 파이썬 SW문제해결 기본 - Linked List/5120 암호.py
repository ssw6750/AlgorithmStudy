# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = 1
    for i in range(0, K):
        idx = (idx+M-1)%N
        if idx == 0:
            idx = N
            arr.append(arr[idx-1]+arr[0])
        else: arr.insert(idx, arr[idx-1]+arr[idx])
        N+=1
        idx +=1

    arr.reverse()
    print("#{} {}".format(test_case, str(arr[:10])[1:-1].replace(',','')))
