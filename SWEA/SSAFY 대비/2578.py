import sys
input = sys.stdin.readline

mtx = []
nums = []
bgcheck = [0] * 12

for i in range(5):
    mtx.append(list(map(int, input().split())))

for i in range(5):
    nums.append(list(map(int, input().split())))

v = [[0]*5 for _ in range(5)]
ans = 0

for i in range(5):
    for j in range(5):
        ans+=1
        num = nums[i][j]
        f = False
        for ii in range(5):
            for jj in range(5):
                if  mtx[ii][jj] == num:
                    v[ii][jj] = 1
                    f = True
                    break
            if f: break  

        for ii in range(5):
            check = 0
            for jj in range(5):
                check += v[ii][jj]
            if check == 5:
                bgcheck[ii] = 1     

        for ii in range(5):
            check = 0
            for jj in range(5):
                check += v[jj][ii]
            if check == 5:
                bgcheck[ii+5] = 1

        check = 0
        for ii in range(5):
            check += v[ii][ii]
        if check == 5:
            bgcheck[10] = 1

        check = 0
        for ii in range(5):
            check += v[ii][4-ii]
        if check == 5:
            bgcheck[11] = 1

        if sum(bgcheck)>=3:
            print(ans)
            exit()


