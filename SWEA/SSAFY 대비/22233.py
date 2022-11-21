import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input().replace("\n", ""))

for _ in range(m):
    a = input().replace("\n", "")
    tmp = list(a.split(","))
    for i in tmp:
        s.discard(i)
    print(len(s))