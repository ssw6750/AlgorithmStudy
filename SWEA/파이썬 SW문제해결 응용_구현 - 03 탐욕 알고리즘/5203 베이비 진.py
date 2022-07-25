def F(lst, i):
    if lst[i] >= 3:
        return True
    if lst[i - 2] and lst[i - 1] and lst[i]:
        return True
    if i < 8 and lst[i] and lst[i + 1] and lst[i + 2]:
        return True
    if i < 9 and lst[i - 1] and lst[i] and lst[i + 1]:
        return True
    return False

T = int(input())
for test_case in range(1, T+1):
    N = list(map(int, input().split()))
    c1 = [0] * 10
    c2 = [0] * 10

    i = 0
    a = 0

    for i in range(0, 12):
        if i % 2 == 0:
            c1[N[i]] += 1
            if F(c1, N[i]):
                a = 1
                break
        else:
            c2[N[i]] += 1
            if F(c2, N[i]):
                a = 2
                break
    print('#{} {}'.format(test_case, a))