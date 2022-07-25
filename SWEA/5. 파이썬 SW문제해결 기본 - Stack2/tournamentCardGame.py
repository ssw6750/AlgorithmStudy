#합병정렬


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    l = list(map(int, input().split()))

    def rps(n1, n2):  # 가위바위보
        a = l[n1-1]
        b = l[n2-1]
        if a == b:
            return n1
        if a - b > 0:
            if abs(a-b) ==2:
                return n2
            else : 
                return n1
        else:
            if abs(a-b) ==2:
                return n1
            else : 
                return n2

    def dv(i, j):  # 로직...
        if i == j:
            return i
        i2 = dv(i, (i+j)//2)
        j2 = dv((i+j)//2+1, j)
        return rps(i2, j2)
    
    print("#{} {}".format(test_case, dv(1, N)))



        


