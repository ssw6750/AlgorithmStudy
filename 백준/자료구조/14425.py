# 교집합에서 중복 요소가 제거됨
# n, m = map(int, input().split())
# s1=set()
# s2=set()
# for i in range(n):
#     s1.add(input())
# for i in range(m):
#     s2.add(input())

# print(s1&s2)
# print(len(s1&s2))

n, m = map(int, input().split())
arr=[]
dic = {}
ans = 0
for i in range(n):
    arr.append(input())
for i in range(m):
    tmp = input()
    if tmp in dic:
        dic[tmp] +=1
    else: dic[tmp] = 1

for i in range(n):
    if arr[i] in dic:
        ans+=dic[arr[i]]

print(ans)


