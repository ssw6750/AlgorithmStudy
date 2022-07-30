def F(a, b):
    global tmp
    if b%3==0:
        tmp+=a
        tmp+=b//3
        return
    else:
        if a<=0:
            tmp=-1
            return
        else:
            F(a-1, b+5)

import sys
input = sys.stdin.readline

n = int(input())
a, b = divmod(n, 5)
tmp = 0
F(a, b)
print(tmp)