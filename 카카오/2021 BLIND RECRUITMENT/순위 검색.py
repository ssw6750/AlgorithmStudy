# 채점 결과
# 정확성: 40.0
# 효율성: 0.0
# 합계: 40.0 / 100.0

def solution(info, query):
    answer = []
    info_arr = []
    query_arr = []
    for i in info:
        info_arr.append(i.split(" "))
    for i in query:
        tmp = i.split(" and ")
        tmp2 = tmp.pop().split(" ")
        tmp.append(tmp2[0])
        tmp.append(tmp2[1])
        query_arr.append(tmp)
        
    for i in query_arr:
        cnt = 0
        for j in info_arr:
            if int(i[4]) <= int(j[4]):
                for k in range(4):
                    f = True
                    if i[k] == '-':
                        continue
                    else:
                        if i[k] != j[k]:
                            f = False
                            break
                if f == True:   
                    cnt+=1
        answer.append(cnt)
    return answer