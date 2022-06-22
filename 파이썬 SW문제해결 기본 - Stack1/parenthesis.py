T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    a = 1
    d = {')':'(', '}':'{'}
    stack = []

    def push(item):
        stack.append(item)

    def pop(item):
        if len(stack)<=0 or d[item] != stack[-1]:
            return 0
        else :
            return stack.pop(-1)
        
    for i in str1:
        if i == '(' or i == '{':
            push(i)
        if i == ')' or i == '}':
            if pop(i) == 0:
                a = 0
                break

    if len(stack)!=0:
        a=0
    
    print("#{} {}".format(test_case, a))


