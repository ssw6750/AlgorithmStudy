T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))

    c.sort()
    c.reverse()
    t.sort()
    t.reverse()

    w=0

    for i in range(len(t)):
        for j in range(len(c)):
            if c[j] <= t[i]:
                w+=c[j]
                c.remove(c[j])
                break
            
    print("#{} {}".format(test_case, w))