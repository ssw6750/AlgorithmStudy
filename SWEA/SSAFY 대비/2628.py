import sys
input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input())
ar_w = [0, w]
ar_h = [0, h]

for i in range(n):
    t, k = map(int, input().split())
    if t:
        ar_w.append(k)
    else:
        ar_h.append(k)

ar_w.sort()
ar_h.sort()


mx = 0

for i in range(len(ar_w)-1):
    for j in range(len(ar_h)-1):
        tmp = (ar_w[i+1] - ar_w[i]) * (ar_h[j+1] - ar_h[j])
        if tmp > mx:
            mx = tmp

print(mx)