import sys
sys.setrecursionlimit(10**6)

n = int(input())

def f(n):
    global memo
    if n >= 3 and len(memo) <=n:
        memo.append(f(n-1)+f(n-2)*2)
    return memo[n]

memo = [0, 1, 3]
print(f(n)%10007)