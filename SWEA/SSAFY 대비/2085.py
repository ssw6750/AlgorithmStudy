for t in range(1, int(input())+1):
    n = int(input())
    ar = []
    for _ in range(n):
        ar.append(list(map(int, input().strip())))

    nn = (n-1)//2
    ans = 0
    idx = 0

    while(nn > 0):
        ans+= sum(ar[idx][nn:n-nn]) + sum(ar[-1-idx][nn:n-nn]) 
        nn-=1
        idx+=1

    ans+=sum(ar[idx])
    print('#{} {}'.format(t, ans))
