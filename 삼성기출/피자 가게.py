# 상 하 좌 우
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

import sys
input = sys.stdin.readline
from copy import deepcopy

n, kk = map(int, input().split())
ar = list(map(int, input().split()))
cnt = 0

# (시계방향 90도) 리스트 회전
def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

while(True):
    # print("~~~~~~~~~~~~~~~~~")
    cnt+=1
    # 밀가루 양이 가장 작은 위치에 밀가루 1만큼 더 넣어주기
    mn = 3001
    tmp1 = []
    for i in range(len(ar)):
        if ar[i] < mn:
            mn = ar[i]
            tmp1 = [i]
        elif ar[i] == mn:
            tmp1.append(i)

    for i in tmp1:
        ar[i] +=1


    # 도우 말기
    d = []
    tmp2 = [[ar[0]], ar[1:]] # 리스트 크기 1만큼 분리
    while True:
        tmp3 = tmp2[:-1]    # tmp3 : 말아올리는 도우 리스트 -> 일단 밑단을 제외한 도우를 가져옴
        lot = tmp2[-1][:len(tmp3[0])] # 밑단에서 떼어온 상단 도우의 길이만큼 도우를 분리함
        tmp3.append(lot)
        last = tmp2[-1][len(tmp3[0]):] # 말지 않는 나머지 도우
        tmp2 = rotated(tmp3)+[last] # 나머지 도우 위에다 말은 도우를 올림
        if len(tmp2[-2])<=len(tmp2[-1]):
            d=tmp2
        else: break # 위에 있는 도우의 너비가 더 넓어지면 중단 


    # 도우 눌러주기
    v = deepcopy(d) # v: 인접한 밀가루가 중복되지 않도록 기록 (상,하,좌,우)
    for i in range(len(d)):
        for j in range(len(d[i])):
            v[i][j] = [0,0,0,0]

    copy_d = deepcopy(d) # 기존 밀가루 훼손 x
    for i in range(len(d)):
        for j in range(len(d[i])):
            for k in range(4):
                yy = i+dy[k]
                xx = j+dx[k]
                if 0<= yy <len(d) and 0<= xx <len(d[yy]) :
                    if v[i][j][k] == 0:
                        v[i][j][k] =1               # 내위치와 방향을 기록
                        v[yy][xx][(k+2)%4] =1       # 상대방 위치의 반대 방향을 기록
                        a = abs(d[i][j]-d[yy][xx])//5
                        if a>0:
                            if d[i][j]>d[yy][xx]:
                                a*=-1
                            copy_d[i][j] +=a
                            copy_d[yy][xx] -=a


    d = deepcopy(copy_d)

    # 1자로 펴기 (도우 말기랑 동일하게 분리 후 말기)
    tmp4 = d[:-1]
    a = d[-1][:len(tmp4[0])]
    b = d[-1][len(tmp4[0]):]
    tmp4.append(a)
    tmp4 = rotated(tmp4)

    # 조건에 맞게 배치 (열이 작은 것 부터 먼저 나열하며, 열이 같다면 행이 작은 것)
    tmp5 = []
    for i in tmp4:
        for j in i:
            tmp5.append(j)

    d = tmp5+b


    # 도우를 두 번 반으로 접기
    l = d[:len(d)//2]
    l.reverse()
    r = d[len(d)//2:]
    tmp6 = [l] + [r]

    # print(tmp6)

    tmp7 = []
    tmp8 = []
    for i in tmp6:
        # print("AA")
        # print(i)
        a = i[:len(i)//2]
        b = i[len(i)//2:]
        a.reverse()
        tmp7.append(a)
        tmp8.append(b)

    tmp7.reverse()
    d = tmp7+tmp8
    # print(d)


    # 도우 눌러주기 (기존과 동일한 방법)
    v = deepcopy(d)
    for i in range(len(d)):
        for j in range(len(d[i])):
            v[i][j] = [0,0,0,0]

    copy_d = deepcopy(d)
    for i in range(len(d)):
        for j in range(len(d[i])):
            for k in range(4):
                yy = i+dy[k]
                xx = j+dx[k]
                if 0<= yy <len(d) and 0<= xx <len(d[yy]) :
                    if v[i][j][k] == 0:
                        v[i][j][k] =1
                        v[yy][xx][(k+2)%4] =1
                        a = abs(d[i][j]-d[yy][xx])//5
                        if a>0:
                            if d[i][j]>d[yy][xx]:
                                a*=-1
                            copy_d[i][j] +=a
                            copy_d[yy][xx] -=a


    d = deepcopy(copy_d)

    tmp4 = d[:-1]
    a = d[-1][:len(tmp4[0])]
    b = d[-1][len(tmp4[0]):]
    tmp4.append(a)
    tmp4 = rotated(tmp4)
    tmp5 = []
    for i in tmp4:
        for j in i:
            tmp5.append(j)

    d = tmp5+b
    ar = deepcopy(d)


    if max(ar) - min(ar) <= kk:
        break

print(cnt)