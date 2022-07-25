# 5108. [파이썬 S/W 문제해결 기본] 7일차 - 숫자 추가

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(0, M):
        tmp = list(map(int, input().split()))
        arr.insert(tmp[0], tmp[1])                  #insert() 사용


    print("#{} {}".format(test_case, arr[L]))