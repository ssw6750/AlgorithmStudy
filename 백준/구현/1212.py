import sys
input = sys.stdin.readline  

N = input()
t = int(N, 8)
print(bin(t)[2:])