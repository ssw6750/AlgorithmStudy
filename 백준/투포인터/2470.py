import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
i = 0
j = N - 1
mn = (10**9)*2
t = []
# print(arr)
while True:
    if i >= j:
        break
    tmp = arr[i] + arr[j]
    # print(arr[i], arr[j], abs(tmp))
    if abs(tmp) < mn:
        mn = abs(tmp)
        t = [i, j]
    if tmp < 0 and i+1-j != 0:
        i += 1
    elif tmp > 0 and i-j-1 != 0:
        j -= 1
    else:
        break

print(arr[t[0]], arr[t[1]])