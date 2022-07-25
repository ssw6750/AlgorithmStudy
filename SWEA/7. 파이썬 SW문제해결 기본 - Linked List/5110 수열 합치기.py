# 5110. [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    l = []
    for i in range(0, M):
        if i == 0:
            arr=list(map(int, input().split()))
        else:         
            tmp = list(map(int, input().split()))
            for s in range(0,len(arr)):
                if arr[s]>tmp[0]:
                    # arr = arr[0:s] + tmp + arr[s:] # 제한시간 초과....
                    arr[s:s] = tmp
                    break
            else: arr = arr + tmp # extend() 쓰면 더 빠름

    arr.reverse()

    print("#{} {}".format(test_case, str(arr[:10])[1:-1].replace(',','')))
