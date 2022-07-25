import copy

def recur(subset, i, arr):	      
  if i == len(arr): 		     # 재귀함수의 탈출조건
    result.append(copy.copy(subset)) # 결과에 들어가는 모든 원소에 해당하는 부분집합의 레퍼런스가 
    return			     # subset으로 같기 때문에 subset을 카피하여 넣어줘야 한다.
				     # 이렇게 하지 않으면 result에 들어가는 모든 부분집합이 공집합으로 나온다.
  else:
    subset.append(arr[i])
    i += 1
    recur(subset, i, arr) 	     # i번째 원소가 '있을' 때의 경우에서 분화
    subset.pop()					
    recur(subset, i, arr)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result=[]
    ar=[]
    N, M = map(int, input().split())
    for i in range(N):
        ar.append(i+1)
    
    recur([], 0, ar)

    print("#{} {}".format(test_case, mv))
