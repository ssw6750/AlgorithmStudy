from termios import N_SLIP


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = [], []

    for i in range(N):
        A.append(input())
    for i in range(M):
        B.append(input())
    
    cnt = 0
    for pf in B:
        for string in A:
            if pf == string[:len(pf)]:
                cnt += 1
                break

    print("#{} {}".format(test_case, cnt))