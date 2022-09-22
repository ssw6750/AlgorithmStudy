import sys
input = sys.stdin.readline

def F(cnt, loc, total):
    global mn
    if cnt == n:
        total = total+arr[loc][0]
        if total < mn:
            mn = total
    if total < mn:
        for i in range(1, n):
            if not v[i]: # 방문 x
                if arr[loc][i]: # 같은 위치 (이동거리 0)이 아닐때
                    v[i] = 1
                    F(cnt+1, i, total+arr[loc][i]) 
                    v[i] = 0 # 다시 원래대로 필수

        

for T in range(int(input())):
    n = int(input())
    v = [0 for _ in range(n)]
    arr = []
    mn = 10**9
    for i in range(n):
        arr.append(list(map(int, input().split())))
    F(1, 0, 0)
    

    print(mn)

