import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    ans = ""
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))

    ar1 = ar1[1:]
    ar2 = ar2[1:]

    if ar1.count(4) > ar2.count(4):
        print("A")
    elif ar1.count(4) < ar2.count(4):
        print("B")
    else:
        if ar1.count(3) > ar2.count(3):
            print("A")
        elif ar1.count(3) < ar2.count(3):
            print("B")
        else:
            if ar1.count(2) > ar2.count(2):
                print("A")
            elif ar1.count(2) < ar2.count(2):
                print("B")
            else:
                if ar1.count(1) > ar2.count(1):
                    print("A")
                elif ar1.count(1) < ar2.count(1):
                    print("B")
                else:
                    print("D")


