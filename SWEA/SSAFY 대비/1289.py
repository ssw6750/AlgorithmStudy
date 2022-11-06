for t in range(1, int(input())+1):
    s = input()
    ar = list(s.strip())
    ans = 0
    f = 1
    for i in range(len(ar)):
        if f:
            if ar[i] == str(f):
                f = 0
                ans+=1
        else:
            if ar[i] == str(f):
                f = 1
                ans+=1
        
    print('#{} {}'.format(t, ans))

    