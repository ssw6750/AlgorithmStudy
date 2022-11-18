import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rsplit())
ar = [int(input().rstrip()) for _ in range(n)]
ans = 0

for i in range(n):
    tmp = set()
    for j in range(i, i+k):
        j = j%n
        tmp.add(ar[j])
    cnt = len(tmp)
    if c not in tmp:   
        cnt+=1
    ans = max(ans, cnt)

print(ans)
