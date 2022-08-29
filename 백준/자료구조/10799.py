import sys
input = sys.stdin.readline

e = list(input())
stack = []
cnt = 0
for i in range(len(e)):
    if e[i] == '(':
        stack.append(e[i])
    elif e[i] == ')':
        if e[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt+=1

print(cnt)
