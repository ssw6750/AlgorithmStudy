import sys
input = sys.stdin.readline

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    ar = list(map(int, input().split()))
    idx = len(ar) - 1
    money = 0

    while idx > 0:
        for i in range(idx-1, -1, -1):
            if ar[idx] > ar[i]:
                money += ar[idx] - ar[i]
            else:
                idx = i
                break
        else:
            break

    print('#{} {}'.format(test_case, money))