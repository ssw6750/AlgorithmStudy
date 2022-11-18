# 시간 초과

# dy = [-1, -1, 1, -1]  
# dx = [1, -1, -1, -1]

# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())

# x = p
# y = h - q
# dir = 0
# ans = 0

# while True:
#     if ans == t: break
#     while True:
#         nx = x+dx[dir]
#         ny = y+dy[dir]
#         if nx < 0 or ny < 0 or ny > h or nx > w:
#             dir = (dir+1)%4
#         else:
#             break
#     x = nx
#     y = ny
#     ans+=1

# print(nx, h-ny)


# (w * h 격자)
w, h = map(int, input().split())

# 처음 개미의 위치 (p,q)
p, q = map(int, input().split())

# 개미가 움직인 시간
t = int(input())

# 개미가 이동한 거리 - 왕복한 거리
a = (p + t) // w
b = (q + t) // h

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
