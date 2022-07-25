def bino_coef(n, k):
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1]+B[i-1][j]

    return B[n][k]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, a, b = map(int, input().split())
    B = [[0]*(n+1) for i in range(n+1)]
    print("#{} {}".format(test_case, bino_coef(n,a)))
    