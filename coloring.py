T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    K = []
    for i in range(0,n):
        tmp = list(map(int, input().split()))
        K.append(tmp)

    # arr = [[0]*10]*10 x -> 얕은복사 개념
    # https://velog.io/@sjy5386/Python-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8%ED%95%98%EA%B8%B0

    arr = [[0 for j in range(10)] for i in range(10)] # 2차원 배열 선언
    count = 0

    for s in range(0, n):
        for j in range(K[s][0], K[s][2]+1):
            for k in range(K[s][1], K[s][3]+1):
                if arr[k][j] == 0:                      # 색칠되어 있지 않으면 현재 색(1, 2)으로 색칠하기
                    arr[k][j] = arr[k][j]+K[s][4]
                elif arr[k][j] == 1 and K[s][4] == 2:   # 빨강(1)로 색칠되어 있고 현재 색이 파랑(2)이면 count 증가
                    arr[k][j] += K[s][4]                # 보라(3)로 색칠
                    count+=1
                elif arr[k][j] == 2 and K[s][4] == 1:   # 파랑(2)로 색칠되어 있고 현재 색이 빨강(1)이면 count 증가
                    arr[k][j] += K[s][4]                # 보라(3)로 색칠
                    count+=1

    print(('#{} {}').format(test_case, count))

