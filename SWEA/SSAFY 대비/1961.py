#출력문

def rotate(A, B):
    for i in range(n):
        for j in range(n):
            B[j][n - 1 - i] = A[i][j]

for t in range(1, int(input())+1):
    n = int(input())
    ar = [list(map(int, input().split())) for _ in range(n)]

    ar1 = [[0] * n for _ in range(n)]
    rotate(ar, ar1)
    ar2 = [[0] * n for _ in range(n)]
    rotate(ar1, ar2)
    ar3 = [[0] * n for _ in range(n)]
    rotate(ar2, ar3)


    print("#{}".format(t))
    for i in range(n):
        print(''.join(map(str, ar1[i])), end=" ")
        print(''.join(map(str, ar2[i])), end=" ")
        print(''.join(map(str, ar3[i])), end=" ")
        print()