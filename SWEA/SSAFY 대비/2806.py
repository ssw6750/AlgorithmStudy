# def dfs(y):
#     if y == N:
#         global count
#         count += 1
#         return

#     for x in range(N):
#         if row[x] or diag1[x + y] or diag2[x - y]:
#             continue

#         row[x] = diag1[x + y] = diag2[x - y]= 1
#         dfs(y+1)
#         row[x] = diag1[x + y] = diag2[x - y]= 0


# T = int(input())

# for tc in range(T):
#     N = int(input())
#     count = 0
#     row, diag1, diag2 = [0 for _ in range(N)], [0 for _ in range(2 * N - 1)], [0 for _ in range(2 * N - 1)]

#     dfs(0)

#     print('#{} {}'.format(tc+1, count))

def dfs(idx):
    global ans
    if idx == N:
        ans +=1
        return
    for i in range(N): # 세로 순환
        f = False
        if v[i]: continue  # 가로 세로 체크
        for j in range(idx): # 대각선 체크
            if idx-j == abs(i-mtx[j]): 
                f=True
                break
        if f: continue
        v[i] = 1
        mtx[idx] = i
        dfs(idx+1)
        v[i] = 0

for t in range(1, int(input()) + 1):
    N = int(input())
    mtx = [0 for _ in range(N)]
    v = [0 for _ in range(N)]
    ans = 0

    dfs(0)
    print('#{} {}'.format(t, ans))

