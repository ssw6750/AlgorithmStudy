T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    a = 0
    if str2.find(str1) != -1:
        a = 1

    print("#{} {}".format(test_case, a))
    