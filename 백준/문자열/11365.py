import sys
input = sys.stdin.readline

while True:
    a = input()
    if a == "END\n":
        break
    print(a[-2::-1])