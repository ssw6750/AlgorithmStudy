for t in range(1, int(input())+1):
    s = input()
    i = 1
    while True:
        if s[0:i] == s[i:2*i]:
            break
        i+=1
    print('#{} {}'.format(t, i))
    
