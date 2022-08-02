import sys
input = sys.stdin.readline  

r = [-1, 1, 0, 0]
c = [0, 0, 1, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N**2)]
seats = [[0]*N for _ in range(N)]

for o in range (N**2):  # 자리 순회
    tmp = []
    for i in range(N):
        for j in range(N):
            # 해당 자리 확인
            if seats[i][j] == 0:
                e = 0
                l = 0 
                for k in range(4):  #해당 자리의 주변 자리 체크(8방향)
                    nr = i+r[k]
                    nc = j+c[k]
                    if (nr >= 0 and nr <= N-1) and (nc >= 0 and nc <= N-1):   # 자리의 범위 확인
                        if  seats[nr][nc] == 0:    # 자리지정x
                            e+=1
                        elif seats[nr][nc] in arr[o][1:]: # 좋아하는 학생 존재
                            l+=1
                tmp.append([l, e, i, j]) # 해당 자리(seats[i][j])를 기준으로 빈자리와 좋아하는 사람 체크
    tmp.sort(key=lambda x : (x[0], x[1], -x[2], -x[3])) # 조건에 맞게 정렬
    seats[tmp[-1][2]][tmp[-1][3]] = arr[o][0] #= 최적의 조건에 자리 배정

ans = 0
for k in range(N):
    for i in range(N):
        sum=0
        idx = -1
        for o in range(N**2):
            if seats[k][i] == arr[o][0]:
                idx = o
                break
        for j in range(4):
            nr = k+r[j]
            nc = i+c[j]
            if  (nr >= 0 and nr <= N-1) and (nc >= 0 and nc <= N-1):
                if seats[nr][nc] in arr[o][1:]:
                    sum+=1
        if sum > 0:
            ans += (10**(sum-1))
print(ans)


        




