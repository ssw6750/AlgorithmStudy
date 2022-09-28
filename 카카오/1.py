from collections import defaultdict
from datetime import datetime

def F(day, t, term, today):
    tmp = term[t]
    tmp = int(tmp) * 28
    print(tmp)
    y, m, d = day.split(".")
    y1, m1, d1 = today.split(".")
    dd = int(m)*28 + int(d)
    td = int(m1)*28 + int(d1)

    if y == y1:
        deff = td - dd
    else:
        deff = (int(y1) -int(y) - 1) * (28 * 12) + td + (28 * 12) - dd

    print(deff)
    return (tmp <= deff)




def solution(today, terms, privacies):
    answer = []

    term = defaultdict()
    for i in terms:
        a, b = i.split(" ")
        term[a] = b
    
    print(term)

    for i in range(len(privacies)):
        day, t = privacies[i].split(" ")
        if F(day, t, term, today):
            answer.append(i+1)

    return answer

def solution(cap, n, deliveries, pickups):
    answer = -1
    cnt = 0
    
    mx = n-1
    while True:
        if sum(deliveries) + sum(pickups) == 0: break
        c = cap
        d = 0
        for i in range(mx, -1, -1):
            if deliveries[i] > 0:
                if c - deliveries[i] >= 0:
                    if i+1 > d:
                        d = i+1
                    c -= deliveries[i]
                    deliveries[i] = 0

        for i in range(mx, -1, -1):
            if pickups[i] > 0:
                if c + pickups[i] <= cap:
                    if i+1 > d:
                        d = i+1
                    c += pickups[i]
                    pickups[i] = 0
        cnt+= d

    answer = cnt*2      


    return answer

    def solution(cap, n, deliveries, pickups):
    answer = -1
    ar = []
    for i in range(n):
        ar.append([deliveries[i], pickups[i]])

    print(ar)
    return answer





    def F(cap, idx):
    if idx < 0: break
    if deliveries[idx] < 0:
        F(cap, idx-1)
    if cap - deliveries[idx] >= 0:
        deliveries[idx] = 0
        F(cap -= deliveries[idx], idx-1)
    else:
        F(cap, idx-1)

def solution(cap, n, deliveries, pickups):
    answer = -1
    while True:
        tmp = []
        F(cap, )
   

    return answer


    def solution(users, emoticons):
    answer = []
    dc = [10, 20, 30, 40]
    mx_plus_user = 0
    emo_sum = sum(emoticons) 

    for i in user:
        d = i[0]
        if d%10 == 0:
            d = d//10 -1
        else:
            d = int(d//10) - 1 
        if emo_sum * 0.6 <i[1]: # 가장 많이 할인했을때 일정가격 보다 작으면 -> 절대 이모티콘 플러스를 사지 않음
            continue
        else: #



    return answer

