T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())
    ca = 0
    cb = 0
    a = ''

    l=1  
    r=P      
    while(True):
        c = int((l+r)/2)
        if A == c:
            break
        elif A < c:
            r = int((l+r)/2)
            ca+=1
        elif A > c:
            l = int((l+r)/2)
            ca+=1

    l=1  
    r=P 
    while(True):
        c = int((l+r)/2)
        if B == c:
            break
        elif B < c:
            r = int((l+r)/2)
            cb+=1
        elif B > c:
            l = int((l+r)/2)
            cb+=1

    if ca - cb > 0:
        a = 'B'
    elif ca - cb < 0:
        a = 'A'
    else :
        a = 0

    print('#{} {}'.format(test_case, a))
        
