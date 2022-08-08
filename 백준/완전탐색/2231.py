import sys
input = sys.stdin.readline  

n = int(input())
ans = 0

for i in range(1, n + 1):
    tmp = i + sum(map(int,str(i)))

    if tmp == n:
        ans = i
        break

print(ans)