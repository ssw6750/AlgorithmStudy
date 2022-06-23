T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = set(input())
    str2 = input()
    d = {}

    for i in str1:
        cnt = 0
        for j in str2:
            if i==j:
                cnt+=1      
            d[i] = cnt


    print("#{} {}".format(test_case, max(list(d.values()))))