def check(v):
    for i in range(1, 10):
        if v[i] != 1:
                return True
    return False


for t in range(1, int(input())+1):
    mtx = []
    ans = 1
    for _ in range(9):
        mtx.append(list(map(int, input().split())))

    for i in range(9):
        v = [0]*10
        for j in range(9):
            v[mtx[i][j]] +=1
        if check(v):
            ans = 0
            break
            

    for i in range(9):
        v = [0]*10
        for j in range(9):
            v[mtx[j][i]] +=1
        if check(v):
            ans = 0
            break
            

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            v = [0]*10
            for ii in range(3):
                for jj in range(3):
                    v[mtx[i+ii][j+jj]] +=1
            if check(v):
                ans = 0
                break
                

    print('#{} {}'.format(t, ans))
    