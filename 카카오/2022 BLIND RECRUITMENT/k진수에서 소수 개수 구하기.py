def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
def isPrime(n):
    if n == 1:
        return False
    f = True
    for i in range(2, n):
        if i*i > n:
            break
        if n%i == 0:
            f = False
            break
    return f

def solution(n, k):
    answer = 0
    n = convert(n, k)
    print(n)
    
    ar = str(n).split('0')
    
    for i in ar:
        if i == (""): continue
        if isPrime(int(i)):
            answer +=1
        
    
    return answer