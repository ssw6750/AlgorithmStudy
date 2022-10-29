for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    ar = []
    for _ in range(n):
        ar.append(list(map(int, input().split())))
    ans = 0

    for i in range(n):
        c = 0
        for j in range(n):
            if ar[i][j] == 1:
                c+=1
            if ar[i][j] == 0 or j == n-1:
                if c == k:
                    ans+=1
                c = 0
        for j in range(n):
            if ar[j][i] == 1:
                c+=1
            if ar[j][i] == 0 or j == n-1:
                if c == k:
                    ans+=1
                c = 0
    
    print('#{} {}'.format(t, ans))