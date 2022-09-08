# 올바른 괄호인지 체크
def check(p):
    q = []
    for i in range(len(p)):
        if p[i] == '(':
            q.append(p[i])
        else:
            if len(q) <= 0:
                return False
            else: q.pop()
        
    if len(q) == 0:
        return True
    else: return False

# 분리      
def dv(p):
    a = 0
    b = 0
    for i in range(0, len(p)):
        if p[i] == '(':
            a +=1
        else: b+=1
        if a==b:
            return [p[:i+1], p[i+1:]]

# 4-4 수행        
def rv(p):
    p = p[1:-1]
    tmp = ""
    for i in range(len(p)):
        if p[i] == ')':
            tmp+='('
        else:
            tmp+=')'
    return tmp
        
def F(p):
    if p == "":
        return ""
    ar = dv(p)
    if check(ar[0]):
        return ar[0] + F(ar[1])
    else:
        return '(' + F(ar[1]) + ')' + rv(ar[0])

        

def solution(p):
    answer = ''
    answer = F(p)
    return answer