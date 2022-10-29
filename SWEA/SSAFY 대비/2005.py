for t in range(1, int(input())+1) :
    N = int(input())

    p = [ [1], [1,1] ]
    for i in range(2, N) :
        list = [1]
        for j in range(i-1) :
            list += [p[i-1][j] + p[i-1][j+1]]
        list += [1]
        p += [list]

    print("#{}".format(t))
    for i in range(N) :
        print(*p[i])