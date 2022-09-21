import sys
input = sys.stdin.readline

def F(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return F(n-1) + F(n-2) + F(n-3)

for _ in range(int(input())):
    print(F(int(input())))