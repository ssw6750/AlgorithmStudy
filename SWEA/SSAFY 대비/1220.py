# N극 1, S극 2

for t in range(1, 10+1):
    n = int(input())
    mtx = [list(map(int, input().split())) for _ in range(n)]
    count = 0
    for j in range(n):
        temp_stack = []
        check = False
        #아래부터 위로 진행하면서 찾는다.
        for i in range(n):
            if mtx[i][j] == 1: #상단부터 N극 찾기 -> S극이면 N극쪽으로 사라짐
                temp_stack.append(1)
            if mtx[i][j] == 2 and temp_stack: # S극과 N극이 있으면
                temp_stack.clear()
                count += 1
 
    print("#{} {}".format(t, count)) 