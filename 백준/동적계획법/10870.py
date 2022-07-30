import sys
input = sys.stdin.readline

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2) 

n = int(input())
arr = [0, 1]

print(F(n))