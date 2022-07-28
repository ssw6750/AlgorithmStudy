# extend 쓰는게 더 나을지도...?

import sys
from collections import deque
input = sys.stdin.readline

def F(c, ans):
    if c%2==0:
        for _ in range(c//4):
            ans+="AAAA"
        for _ in range((c&2)//2):
            ans+="BB"
    else:
        ans="-1"
    return ans

n = input()
c = 0
ans = ""

for i in range(len(n)):
    if n[i] == 'X' and i<len(n):
        c+=1
    else:
        if c>0:
            ans=F(c, ans)
            if ans == "-1":
                break
            c = 0
        if i<len(n)-1:
            ans+="."

print(ans)
        