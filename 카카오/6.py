dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def F1(r, c, t, v, mt, visited):
    if visited[r][c] == 0:
        if mt[r][c] == t:
            visited[r][c] = 1
            mt[r][c] = v
            for i in range(4):
                y = r+dy[i]
                x = c+dx[i]
                if 0 < y < len(visited) and 0 < x < len(visited[0]):
                    F1(y, x, t, v, mt, visited)
        else: return


def solution(commands):
    answer = []
    mxr = 0
    mxc = 0
    mt = [["" for _ in range(51)] for _ in range(51)]
    for i in commands:
        visited = [[0 for _ in range(mxr+1)] for _ in range(mxc+1)]
        tmp = list(map(str, i.split(" ")))
        if tmp[0] == "UPDATE":
            if len(tmp) == 4:
                i1, j1, v= int(tmp[1]), int(tmp[2]), tmp[3]
                t= mt[i1][j1]
                if mxr < int(tmp[1]):
                    mxr = int(tmp[1])
                if mxc < int(tmp[2]):
                    mxc = int(tmp[2])
                if t == "":
                    mt[i1][j1] = v
                else:
                    F1(i1, j1, mt[i1][j1], v, mt, visited)
            else:
                t = tmp[1]
                v = tmp[2]
                for i1 in range(mxr+1):
                    for j1 in range(mxc+1):
                        if mt[i1][j1] == t:
                            F1(i1, j1, t, v, mt, visited)
                            break

        if tmp[0] == "MERGE":
            r1, c1, r2, c2 = int(tmp[1]), int(tmp[2]), int(tmp[3]), int(tmp[4])
            v = mt[r1][c1]
            t = mt[r2][c2]
            if t == "":
                mt[r2][c2] = v
            else:
                for i2 in range(mxr+1):
                    for j2 in range(mxc+1):
                        if mt[i2][j2] == t:
                            mt[i2][j2] = v

        if tmp[0] == "UNMERGE":
            r, c = int(tmp[1]), int(tmp[2])
            v = mt[r][c]
            for i3 in range(mxr+1):
                for j3 in range(mxc+1):
                    if mt[i3][j3] == v:
                        if (i3 != r or j3 != c) :
                            mt[i3][j3] = ''

        if tmp[0] == "PRINT":
            r, c = int(tmp[1]), int(tmp[2])
            if mt[r][c] == '':
                answer.append("EMPTY")
            else:
                answer.append(mt[r][c])
        


    return answer