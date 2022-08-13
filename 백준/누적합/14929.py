import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
num = []
num.append(temp[0])
for i in range(1, n):
    num.append(num[i-1] + temp[i])

ans = 0
for i in range(n):
    ans += temp[i] * (num[n-1]-num[i])

print(ans)
