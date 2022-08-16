# 왜 틀리지...
cnt = Counter(s).most_common()


import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
for i in range(n):
    dic = defaultdict(int)
    max = 0
    value = ''
    c = 0
    str = input()
    for i in range(len(str)):
        if str[i] == ' ' or str[i] == '\n': continue
        dic[str[i]]+=1
    for k, v in dic.items():
        if v>max:
            max = v
            value = k
            c=1
        elif v==max:
            c+=1
    if c>1:
        print('?')
    else: print(value)


