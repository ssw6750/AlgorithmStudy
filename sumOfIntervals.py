T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    l = list(map(int, input().split()))

    arr = []

    # 완전탐색
    for i in range(0, N-M+1):
        sum=l[i]
        for j in range(i+1, i+M):
            sum+=l[j]
        arr.append(sum)

    print(('#{} {}').format(test_case, max(arr)-min(arr)))

    