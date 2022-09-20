import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def F(n, turn):
    if (n == 1) or (n == 3):
        return turn

    if turn == "SK":
        turn = "CY"
    else:
        turn = "SK"

    if n == 2:
        return turn


    if n%3 == 0:
        return F(n-1, turn)
    elif n%3 == 1:
        return F(n-1, turn)
    elif n%3 == 2:
        return F(n-3, turn)

n = int(input())

print(F(n, "SK"))


