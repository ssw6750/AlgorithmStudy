import sys
input = sys.stdin.readline

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

n = int(input())
arr = list(map(int, input().split()))
g=gcd(list[0],gcd(list[1],list[-1]))    # 최대 공약수

for i in range(1, g//2+1):
    if g%i==0:
        print(i)
print(g)
