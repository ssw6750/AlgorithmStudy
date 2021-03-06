# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# [입력]

# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
 

# [출력]

# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): 
    K, N, M = map(int, input().split())
    l = list(map(int, input().split()))

    #충전소 정류장과 출발지점, 도착지점을 합친 배열 생성
    l.insert(0, 0)
    l.append(N)
    M=M+2

    count=0     # count 충전소 정류장에 방문하는 횟수
    n=0         # l[n] 현재 버스의 위치
    tmp=1       # l[tmp] 충전소 정류장 위치
   
    while(n<M):
        while(True):
            if l[tmp]-l[n]>K:   #충전소 정류장으로부터 거리가 K초과
                if tmp-n <= 1:  #근접한 정류정이면 정점에 도착할 수 없다고 판단.
                    count=0
                    n=N
                    break
                else:           #l[tmp-1]위치의 충전소 정류장을 방문
                    count+=1
                    n=tmp-1
                    break
            else:               #충전소 정류장으로부터 거리가 K이하
                tmp+=1          # 다음 충전소 정류장 위치 확인 후 다시 루프
                if tmp >=M :    # 도착지점에 도착했으면 종료
                    n=tmp
                    break
    print("#{} {}".format(test_case, count))
                



    
