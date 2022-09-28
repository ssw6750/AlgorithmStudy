# 조건에 맞는 이동방식을 일일이 계산하여 bfs로 풀음
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


from collections import deque

# wall = ["H.H", ".HX", "H.H"]
wall = ["....HH", "H..H.H"]

def BFS(y, x, wall, n1, m, visited):
    if wall[y][x] == 'H':
        cnt = 1
    else:
        cnt = 0
    queue = deque([[[y, x], cnt]])

    while queue:
        n = queue.popleft()
        y1 = n[0][0]
        x1 = n[0][1]
        c = n[1]
        if wall[y1][x1] == 'H': 
            if visited[y1][x1] == 0:
                visited[y1][x1] = c
            else:
                if visited[y1][x1] > c:
                    visited[y1][x1] = c

            # case1 오른쪽 2칸
            if y1-1 >= 0 and x1+2 < n1:
                f = True
                for i in range(3):
                    if wall[y1-1][x1+i] != '.':
                        f = False
                        break
                if wall[y1][x1+1] != '.':
                    f = False
                    break
                if f == True:
                    queue.append([[y1,x1+2],c+1])

            # case2 왼쪽 2칸
            if y1-1 >= 0 and x1-2 >= 0:
                f = True
                for i in range(3):
                    if wall[y1-1][x1-i] != '.':
                        f = False
                        break
                if wall[y1][x1-1] != '.':
                    f = False
                    break
                if f == True:
                    queue.append([[y1,x1-2], c+1])

            # case3 오른쪽 3칸
            if y1-1 >= 0 and x1+3 < n1:
                f = True
                for i in range(4):
                    if wall[y-1][x+i] != '.':
                        f = False
                        break
                if wall[y][x+1] != '.' or wall[y][x+2] != '.':
                    f = False
                    break
                if f == True:
                    queue.append([[y1,x1+3], c+1])

            # case4 왼쪽 3칸
            if y1-1 >= 0 and x1-3 >= 0:
                f = True
                for i in range(4):
                    if wall[y1-1][x1-i] != '.':
                        f = False
                        break
                if wall[y1][x1-1] != '.' or wall[y1][x1-2] != '.':
                    f = False
                    break
                if f == True:
                    queue.append([[y1, x1-3],c+1])

            # case5 위로 2칸
            if y1-2 >=0:
                if wall[y1-1][x1]=='.':
                    queue.append([[y1-2, x1], c+1])

            # case6 오른쪽 대각
            if y1-1 >= 0 and x1+1<n1:
                if wall[y1-1][x1] == '.' and wall[y1][x1+1] == '.':
                    queue.append([[y1-1, x1+1], c+1])

            # case6 왼쪽 대각
            if y1-1 >= 0 and x1-1>=0:
                if wall[y1-1][x1] == '.' and wall[y1][x1-1] == '.':
                    queue.append([[y1-1, x1-1],c+1])

            # 상하좌우
            for i in range(4):
                yy = y1+dy[i]
                xx = x1+dx[i]
                if 0<= yy < m and 0<=xx<n1:
                    queue.append([[yy, xx], c+1])
 

def solution(wall):
    h = len(wall)
    n = len(wall[0])
    visited = [[0 for _ in range(n)] for _ in range(h)]
    answer = [[0 for _ in range(n)] for _ in range(h)]

    BFS(h-1, 0, wall, n, h, visited)

    for i in range(h):
        for j in range(n):
            if wall[i][j] == 'H':
                if visited[i][j] > 0:
                    answer[i][j] = visited[i][j]
                else: answer[i][j] = -1

    print(answer)
                




solution(wall)