# 진법 변환 함수 int()사용하면 간단하게 가능

import sys, math
input = sys.stdin.readline
K = ord('A')-10

N, B= map(str, input().split())
ans = 0
s=0

# for문(range) 문자열 처리...?
for i in N[::-1]:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):
        ans += ((int(B)**s)*(ord(i)-K))
        s+=1
    else: 
        ans += ((int(B)**s)*(int(i)))
        s+=1

print(ans)