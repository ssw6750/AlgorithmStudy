# 소수점이 0이 될 때까지 2를 곱한다. 그렇게 2를 곱했을 때 정수 부분이 2진수가 되고 그 값을 변수에 더해가면 된다. 


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = float(input())

    cnt = 0     # 자리 수 count
    binary = '' # 2진수 저장
    while n > 0:
        temp = n * 2
        binary += str(temp)[0]  # 정수부분 저장
        n = temp - int(temp)    # 소수점 이하 저장
        cnt += 1

        if cnt > 12:    # 13자리 이상이면 중단
            break

    if cnt > 12:    # 13자리 이상이면 overflow 출력
        print('#{} {}'.format(test_case, 'overflow'))
    else:
        print('#{} {}'.format(test_case, binary))


