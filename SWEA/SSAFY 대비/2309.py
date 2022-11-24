import sys
input = sys.stdin.readline

ar = []
for i in range(9):
    ar.append(int(input()))

for i in range(9):
    tmp = ar[:]
    del tmp[i]
    for j in range(8):
        tmp2 = tmp[:]
        del tmp2[j]
        if sum(tmp2) == 100:
            tmp2.sort()
            for k in range(7):
                print(tmp2[k])
            exit()