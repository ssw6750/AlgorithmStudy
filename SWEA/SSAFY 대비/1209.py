for _ in range(10):
    t = int(input())
    ar = [list(map(int,input().split())) for _ in range(100)]
    mx = 0
    for i in range(100):
        ans1 = 0
        ans2 = 0
        for j in range(100):
            ans1 += ar[i][j]
            ans2 += ar[j][i]
        mx = max(ans1,ans2,mx)

    ans3 = 0
    ans4 = 0
    for i in range(100):
        ans3+=ar[i][i]
        ans4+=ar[i][-i-1]
    mx = max(ans3,ans4,mx)
        

    print("#{} {}".format(t,mx))