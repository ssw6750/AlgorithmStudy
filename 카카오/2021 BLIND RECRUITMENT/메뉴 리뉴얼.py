from collections import defaultdict
from itertools import combinations

# menu_list = Counter(menu).most_common()

def solution(orders, course):
    answer = []
    d = defaultdict(int)
    dd = [[] for _ in range(11)]
    
    for i in course:
        for j in orders:
            s = list(combinations(j, i))
            for k in s:
                tmp = ''.join(o for o in sorted(k))
                d[tmp] += 1

    for k, v in d.items():
        if v>=2:
            if dd[len(k)] == []:
                dd[len(k)].append(v)
            else: 
                if dd[len(k)][-1] > v:
                    continue
                elif dd[len(k)][-1] < v:
                    dd[len(k)] = []
                    dd[len(k)].append(v)
                else:
                    continue
                    
    print(dd)
                
    for k, v in d.items():
        if len(dd[len(k)]) > 0:
            if v == dd[len(k)][0]:
                answer.append(k)

            
    answer.sort()
    
    return answer