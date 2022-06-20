T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr=[]
    a = ''
    for i in range (0, N):
        arr.append(input())

    for i in range (0, N):
        for j in range (0, N-M+1):
            l = j
            r = j+M-1
            while (True):
                if arr[i][l] == arr[i][r]:
                    l+=1
                    r-=1                
                else : 
                    l = j
                    r = j+M-1
                    break                  
                if l>r:
                    a = arr[i][j:j+M]
                    break
            while (True):
                if arr[l][i] == arr[r][i]:
                    l+=1
                    r-=1                
                else : break
                if l>r:
                    for k in range (j,j+M): 
                        a+=arr[k][i]
                    break

    print("#{} {}".format(test_case, a))