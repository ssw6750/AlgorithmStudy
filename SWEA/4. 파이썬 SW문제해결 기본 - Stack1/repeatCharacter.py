T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.\

# 오류남 고쳐야함
for test_case in range(1, T + 1):
    str1 = input()
    def f(s): 
        for i in range(0, len(s)-1):        
            if s[i] == s[i+1]:
                s.remove(s[i])
                s.remove(s[i])
                f(s)
                break
    l = list(str1)
    f(l)
    print("#{} {}".format(test_case, len(l)))
        
