# 알 수 없는 입출력 에러...
import sys
dic={}
sum=0

while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp == '': 
        break
    if tmp in dic:
        dic[tmp] +=1
    else: dic[tmp] = 1
    sum+=1

dic = dict(sorted(dic.items()))
for i in dic:
    a = dic[i]
    b = (a / sum * 100)
    print("%s %.4f" %(i, b))

