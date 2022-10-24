T = int(input())

for t in range(1, T+1) :
    n, m  = map(int, input().split())
    mtx = []
    ar = []

    for i in range(n) :
        mtx.append(list(map(int, input().split())))
        
    for i in range(n-m+1) :
        for j in range(n-m+1) :
            cnt = 0
            for k in range(m) :
                for o in range(m) :
                    cnt += mtx[i+k][j+o]
            ar.append(cnt)

    print("#{} {}".format(t, max(ar)))