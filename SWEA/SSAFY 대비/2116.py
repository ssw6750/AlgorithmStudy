import sys
input = sys.stdin.readline

# 옆면 인덱스
t = [
    [1, 2, 3, 4],
    [0, 2, 4, 5],
    [0, 1, 3, 5],
    [0, 2, 4, 5],
    [0 ,1, 3, 5],
    [1, 2, 3, 4]
]

# 상단 인덱스
r = [5, 3, 4, 1, 2, 0]

n = int(input())
d = []
ans = []

for i in range(n):
    d.append(list(map(int, input().split())))

for i in range(6):
    idx = i # 시작 주사위의 하단 인덱스
    mx = 0
    for j in range(n):
        tmp = []
        for k in t[idx]: # 옆면 눈의 개수 중 가장 높은 개수 찾기 
            tmp.append(d[j][k])
        mx+=max(tmp)

        if j >= n-1: break
        e = d[j][r[idx]] # 해당 주사위의 상단 인덱스의 눈의 개수
        idx = d[j+1].index(e) # 와 일치하는 다음 주사위의 하단 인덱스 

    ans.append(mx)

print(max(ans))



