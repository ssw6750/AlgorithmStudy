T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count = 0
    for i in range(1<<12):
        tmp = []
        for j in range(12):
            if(i&(1<<j)):
                tmp.append(arr[j])
        if len(tmp)==N and sum(tmp)==K:
            count+=1

    print(('#{} {}').format(test_case, count))


