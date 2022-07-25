def pop():
    if len(stack)>0:
        return stack.pop(-1)
    else: return 0
    
def push(item):
    stack.append(item)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    stack = []
    a = 'YES'
    for i in str1:
        if i == '(':
            push(i)
        elif i == ')':
            tmp = pop()
            if tmp != '(':
                a='NO'
                break

    if len(stack)>0: a='NO'

    print(a)
            
