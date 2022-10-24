n = int(input())
for i in range(1, n+1):
    c = 0
    c+=str(i).count('3')
    c+=str(i).count('6')
    c+=str(i).count('9')
    if c > 0:
        for j in range(c):
            print("-", end= "")
        print(end= " ")
    else:
        print(i, end= " ")