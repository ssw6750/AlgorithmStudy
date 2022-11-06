#페르마의 소정리
#https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11401-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-3-%EA%B3%A8%EB%93%9C1-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
p = 1000000007

# 팩토리얼 값 계산(나머지 연산 적용)
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % p
    return n

# 거듭제곱 계산(나머지 연산 적용)
def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    
    tmp = square(n, k//2)
    if k % 2:
        return tmp * tmp * n % p
    else:
        return tmp * tmp % p

top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

# 페르마의 소정리 이용해서 조합 공식 곱셈 형태로 변형
print(top * square(bot, p-2) % p)