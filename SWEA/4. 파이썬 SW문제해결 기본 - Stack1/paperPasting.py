T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    def f(n):
        global memo
        if n >=2 and len(memo) <=n:
            memo.append(f(n-1)+f(n-2)*2)
        return memo[n]
    
    memo = [1, 3, 6]

    print("#{} {}".format(test_case, f(int((n-1)/10))))
