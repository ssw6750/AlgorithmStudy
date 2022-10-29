def check(ar):
    l = len(ar)//2
    for i in range(l):
        if ar[i] != ar[-1-i]:
            return False
    return True

for t in range(1, 11):
    n = int(input())
    ans = 0
    mtx = []
    for i in range(8):
        mtx.append(list(map(str, input().strip())))

    for i in range(8):
        for j in range(8-n+1):
            if check(mtx[i][j:j+n]):
                ans+=1

            tmp = []
            for k in range(j,j+n):
                tmp.append(mtx[k][i])
            if check(tmp):
                ans+=1
            

    print('#{} {}'.format(t, ans))
