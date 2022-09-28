import sys
input = sys.stdin.readline
n, T = map(int, input().split())

def gcd(p, q): # 최대공약수 (뉴클리드 호제법)
    if q==0:
        return p
    return gcd(q, p%q)

def get_divisors(x): # 모든 약수 찾기
    res = []
    for i in range(1, x+1):
        if i * i > x: break
        if x % i == 0:
            res.append(i)
            res.append(x // i)

    return res

def solve(A, B, M):
    # (A, B) -> M일 연체료
    K = M // A
    return B * (K+1)

q = [list(map(int, input().split())) for _ in range(n)]
q.sort(key = lambda x: x[0])

money_gcd = 0
for i in range(n):
    money_gcd = gcd(money_gcd, q[i][1])

candidates = get_divisors(money_gcd)
min_ans, max_ans = sys.maxsize, 0
for cand_money in candidates:
    L, R = 1, 1000000
    for time, cost in q:
        K = cost//cand_money -1
        # upper
        if K > 0:
            R = min(R, time//K)

        # lower
        L = max(L, time//(K+1))

    # L < A <= R
    if L >= R:
        continue

    max_ans = max(max_ans, solve(L+1, cand_money, T))
    min_ans = min(min_ans, solve(R, cand_money, T))

if max_ans == 0:
    print(-1)
else:
    print(min_ans, max_ans)

'''
5 27
4 1000
6 1000
21 3000
16 2000
26 3000
'''