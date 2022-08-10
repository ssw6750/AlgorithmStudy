import sys
input = sys.stdin.readline

def dfs(l):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i>=l:
            s.append(i)
            dfs(i)
            s.pop()

n, m = map(int, input().split())
s = []

dfs(0)