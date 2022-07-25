T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    l = list(map(int, input().split()))

    arr = []
    while(len(l)>0):
        if len(arr)%2==0:
            arr.append(l.pop(l.index(max(l))))
        else:
            arr.append(l.pop(l.index(min(l))))

    print('#{} {}'.format(test_case, str(arr[0:10])[1:-1].replace(',','')))