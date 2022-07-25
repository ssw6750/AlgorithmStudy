n, k = map(int, input().split())

arr = []
ans = []
idx = 0
for i in range(n):
    arr.append(i+1)

while(True):
    idx = (idx + k - 1)%len(arr)
    ans.append(arr.pop(idx))
    if len(arr)<=0:
        break

print("<{}>".format(str(ans)[1:-1]))