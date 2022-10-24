import sys
input = sys.stdin.readline

dy = [-2, -1, 1, 2]

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    ar = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2):
        arr = []
        for j in range(4):
            arr.append(ar[i+dy[j]])
        mx = max(arr)
        if ar[i] - mx > 0:
            ans+=(ar[i] - mx)

    print('#{} {}'.format(test_case, ans))
