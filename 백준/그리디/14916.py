import sys
input = sys.stdin.readline

n = int(input())
if n == 1 or n == 3:
    print(-1)
else:
    a, b = divmod(n, 5)
    if b%2==0:
        print(a+b//2)
    else:
        print((a-1)+((b+5)//2))