def solution(N, stages):
    answer = []
    fList = []
    for i in range(N):
        i += 1
        allC = 0
        count = 0
        for j in stages:
            if j >= i:
                allC += 1
                if j == i:
                    count += 1
                    
        if allC == 0:
            fList.append([i, 0])
        else :
            fList.append([i, count/allC])
        
    answer = sorted(fList, key=lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer