#최장 증가 수열 (이진탐색으로도 풀수있...)
def F():
    for i in range(0, len(arr)-1):
        lis[i]=1
        for j in range(0, i):
            if arr[j]<arr[i] and 1+lis[j]>lis[i]:
                lis[i]=1+lis[j]
    return max(lis)
            

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr=list(map(int, input().split()))
    lis=[0]*len(arr)

    print("#{} {}".format(test_case, F()))