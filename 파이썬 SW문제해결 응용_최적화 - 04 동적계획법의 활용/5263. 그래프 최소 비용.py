#플로이드-워샬 알고리즘
def F(D):
    for k in range(0, N):
        for i in range(0, N):
            if i == k: continue
            for j in range(0, N):
                if j == k or j == i: continue
                D[i][j] = min(D[i][k]+D[k][j], D[i][j])
                #i=2 j=1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N=int(input())
    D = []
    for i in range(N):
        D.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            if D[i][j] == 0:
                D[i][j] = 999

    F(D)

    mv = 0
    # mv = max(map(max, D))
    for i in range(N):
        for j in range(N):
            if D[i][j] > mv and D[i][j] != 999:
                mv = D[i][j]

    print("#{} {}".format(test_case, mv))

