#람다식...

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: (x[1], x[0]))
    last_finish = 0
    cnt = 0
    for s, e in arr:
        if s >= last_finish:
            last_finish = e
            cnt += 1
    print('#{} {}'.format(test_case, cnt))
