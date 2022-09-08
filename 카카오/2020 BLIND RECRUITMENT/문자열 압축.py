def solution(s):
    answer = len(s)
    for i in range(1, len(s)) :
        string = ''
        cnt = 1
        p = s[:i]
        
        for j in range(i, len(s), i):
            if p == s[j:j+i]:
                cnt+=1
            else:
                if cnt >= 2:
                    string += (str(cnt) +p)
                else:
                    string += p
                p =  s[j:j+i]
                cnt = 1
        
        if cnt >= 2:
            string += (str(cnt) +p)
        else:
            string += p
        answer = min(answer, len(string))
                
    return answer