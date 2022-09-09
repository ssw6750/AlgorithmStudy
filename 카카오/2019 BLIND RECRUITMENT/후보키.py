from collections import defaultdict
from itertools import combinations

def check(ar, ck): # 최소성 체크
    f1 = True
    for i in ck:
        f2 = True
        for j in i:
            if j not in ar:
                f2 = False
        if f2 == True and len(ar) > len(i):
            f1 = False
    if f1:
        ck.append(ar)

def solution(relation):
    answer = 0
    r = len(relation)
    c = len(relation[0])
    ar = [i for i in range(c)]
    ck = [] # 최소성 체크
    
    for i in range(c):
        tmp = list(list(combinations(ar, i+1)))
        for j in tmp:
            hash_table = defaultdict(int)   # 해시 테이블 사용                    
            for k in relation:
                key = ''
                for o in j:
                    key+= k[o]
                hash_table[key] +=1
            if len(hash_table) == r:
                check(list(j), ck)

    answer= len(ck)                  
       
    return answer