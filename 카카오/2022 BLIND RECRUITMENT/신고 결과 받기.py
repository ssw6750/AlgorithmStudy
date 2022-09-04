# 맞는 코드
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    d = {}
    for i in id_list:
        answer.append(0)
        d[i]=[]
    
    r = defaultdict(int)

    for i in report:
        a, b = i.split()
        if b not in d[a]: 
            d[a].append(b)
            r[b] += 1

    for key, value in d.items():
        idx = id_list.index(key)
        for i in value:
            if r[i] >= k:
                answer[idx]+=1

    return answer


# 틀린코드
from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    d = {}
    for i in id_list:
        answer.append(0)
        d[i]=[]
    
    r = defaultdict(int)

    for i in report:
        a, b = i.split()
        if b not in d[a]: 
            d[a].append(b)
            r[b] += 1

    for i in report:
        a, b = i.split()
        if r[b] >= k:
            answer[id_list.index(a)] +=1

    return answer
