for t in range(1, 11):
    n = int(input())
    ar = list(map(int, input().split()))
    f = True

    for i in range(n):
        mx_idx = ar.index(max(ar))
        mn_idx = ar.index(min(ar))
        if ar[mx_idx] - ar[mn_idx] <= 1:
            ans = (ar[mx_idx] - ar[mn_idx])
            f = False
            break
        else: 
            ar[mx_idx] -=1
            ar[mn_idx] +=1 
    if f:
        mx_idx = ar.index(max(ar))
        mn_idx = ar.index(min(ar))
        ans = (ar[mx_idx] - ar[mn_idx])

    print('#{} {}'.format(t, ans))
