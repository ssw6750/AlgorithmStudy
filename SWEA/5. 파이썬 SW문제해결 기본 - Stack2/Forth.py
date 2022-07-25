T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    l = list(map(str,input().split()))
    stack = []
    arr = ['+', '-', '*', '/']
    i = 0
    a = ''

    def f(a, b, c):
        if c == '+':
            return a + b
        if c == '-':
            return a - b
        if c == '*':
            return a * b
        if c == '/':
            return a // b   #주의
            

    while True:
        if l[i] == '.': break
        if l[i] not in arr:  
            stack.append(l[i])
        else :
            if len(stack) <=1 :
                 a = 'error'
                 break
            n1 = stack.pop()
            n2 = stack.pop()
            # stack.append(str(eval(n2 + l[i] + n1)))       # 이거 왜...
            stack.append(str(f(int(n2), int(n1), l[i])))
        i+=1

    if len(stack) > 1:
        a = 'error'
    if a != 'error':
        a=stack[0]

    print("#{} {}".format(test_case, a))

