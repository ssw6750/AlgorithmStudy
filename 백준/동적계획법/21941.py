import sys
input=sys.stdin.readline

def func(index):
  global origin

  if index>=len(origin): return 0
  if cache[index]!=-1: return cache[index]

  cache[index]=func(index+1)+1

  for recode in r:
    key=recode[0]
    value=recode[1]

    if origin[index:index+len(key)]==key:
      cache[index]=max(cache[index], func(index+len(key))+value)

  return cache[index]

origin=input()[:-1]
m=int(input())
cache=[-1 for _ in range(len(origin)+1)]
r=[]

for _ in range(m):
  r.append(list(map(str,input().split())))
  r[-1][1]=int(r[-1][1])

print(func(0))



# 시간 초과 
# 단어를 1개씩 빼주면서 재귀

# import sys
# input = sys.stdin.readline

# def F(s, score):
#     global mx
#     for i in arr:
#         w = i[0]
#         idx = s.find(w)
#         if idx != -1:
#             tmp = s[:idx]+s[idx+len(w):]
#             if tmp not in v:
#                 v.append(tmp)
#                 F(tmp, score+int(i[1]))
#     score+=len(s.replace("\n",''))
#     if mx<score:
#         mx = score

# s = input()
# n = int(input())
# arr = []
# mx = 0
# v = []
# for i in range(n):
#     arr.append(list(map(str, input().split())))
    
# F(s, 0)
# print(mx)


# import sys
# input = sys.stdin.readline

# def F(s, score):
#     global mx
#     for i in arr:
#         w = i[0]
#         idx = s.find(w)
#         if idx != -1:
#             F(s[:idx]+s[idx+len(w):], score+int(i[1]))
#     score+=len(s.replace("\n",''))
#     if mx<score:
#         mx = score

# s = input()
# n = int(input())
# arr = []
# mx = 0
# for i in range(n):
#     arr.append(list(map(str, input().split())))
    
# F(s, 0)
# print(mx)
