from collections import defaultdict

def convert(t):
    h, m = t.split(":")
    return (int(h)*60 + int(m))

def lift(n):
    if n < 0: return 0
    if n % 1 != 0:
        return int(n)+1
    else: return n

def solution(fees, records):
    answer = []
    d = defaultdict(int)
    default_time, default_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    
    for i in records:
        t, n, h = i.split()
        if h == 'IN':
            d[n] = d[n] - convert(t)
        else:
            d[n] = d[n] + convert(t)
        print(convert(t))    
        
    for k, v in d.items():
        if v <= 0:
            d[k] = d[k] + convert("23:59")
        
    s = sorted(list(zip(d.keys(), d.values())), key = lambda x : x[0]) 
    print(s)
    
    for i in s:
        answer.append(default_fee + lift((i[1]-default_time)/unit_time) * unit_fee)

    
    return answer