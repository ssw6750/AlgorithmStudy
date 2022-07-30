import sys
input = sys.stdin.readline

def F(n):
    if n>2: F(n-1)
    arr.append(arr[n-1]+arr[n-2])

n = int(input())
arr = [0, 1]
F(n)

print(arr[-1])