for t in range(1, int(input())+1):
    ar = list(map(str, input().strip()))
    n = len(ar)
    nn = (n//2)
    ans = 1
    for i in range(nn):
        print(ar[i], ar[-1-i])
        if ar[i] != ar[-1-i]:
            ans=0
            break

    print('#{} {}'.format(t, ans))