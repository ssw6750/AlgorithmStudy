# eval

import sys
input = sys.stdin.readline

n = int(input())
e = input()
ar = []
for i in range(n):
    ar.append(int(input()))

stack = []

for i in e:
    if 'A' <= i <= 'Z' :
        stack.append(ar[ord(i)-ord('A')])
    else:
        if len(stack) < 2: break
        tmp2 = stack.pop()	
        tmp1 = stack.pop()

        if i =='+' :
            stack.append(tmp1+tmp2)
        elif i == '-' :
            stack.append(tmp1-tmp2)
        elif i == '*' :
            stack.append(tmp1*tmp2)
        elif i == '/' :
            stack.append(tmp1/tmp2)

print('%.2f' %stack[0])	