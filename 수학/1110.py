import sys
input = sys.stdin.readline

N = int(input())
n = N
c = 0

while True:
    if n<10:
        n=10*n+n
    else:
        n=str(n)[0:2]
        n=int(n[1]+str(int(n[0])+int(n[1]))[-1])
    c+=1
    if n == N:
        break

print(c)
