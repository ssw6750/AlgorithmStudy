def f(l):
    
        if l[0] == 'I':
            arr.insert(int(l[1]), int(l[2]))
        elif l[0] == 'D':
            del arr[int(l[1])]
        elif l[0] == 'C':
            arr[int(l[1])] = int(l[2])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    l = []
    k = 0

    for i in range (0, M):
        l = list(map(str, input().split()))
        f(l)

    
    try:
        k = arr[L]
    except:
        k = -1

    print("#{} {}".format(test_case, k))



    
