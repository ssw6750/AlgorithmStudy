for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    ans = 0
    if n == m:
        for i in range(n):
            ans+=ar1[i]*ar2[i]
    else:
        ar = []
        if n>m:
            for i in range(n-m+1):
                s = 0
                for j in range(m):
                    s+=ar1[j+i]*ar2[j]
                ar.append(s)
        elif n<m:
            for i in range(m-n+1):
                s = 0
                for j in range(n):
                    s+=ar1[j]*ar2[i+j]
                ar.append(s)
        ans = max(ar)

    print('#{} {}'.format(t, ans))

