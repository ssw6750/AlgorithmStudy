import sys
input = sys.stdin.readline

n = int(input())
ans = []

for i in range(1, n+1):
    f = n
    s = i
    tmp = [n, i]
    
    while True:
        next = f - s
        if next >= 0:
            tmp.append(next)
            f = s
            s = next
        else:
            if len(tmp) > len(ans):
                ans = tmp
            break
print(len(ans))
print(*ans)