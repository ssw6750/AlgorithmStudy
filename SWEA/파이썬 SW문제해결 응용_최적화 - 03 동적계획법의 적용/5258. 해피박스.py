# 배냥문제... 다시 풀기

def F(W, k, cv):
    global mv
    if W>=0:
        if k>=M:
            if mv < cv:
                mv = cv
        else:
            F(W-weight[k], k+1, cv+value[k])
            F(W, k+1, cv)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    weight = []
    value = []
    mv = 0
    N, M = map(int, input().split())
    for i in range(M):
        tmp = list(map(int, input().split()))
        weight.append(tmp[0])
        value.append(tmp[1])
    F(N, 0, 0)

    print("#{} {}".format(test_case, mv))
