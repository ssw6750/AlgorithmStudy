def F(idx, s):
    global ans
    if idx >= n:         
        return
    if s + ar[idx] == k:
        ans += 1
    F(idx + 1, s)
    F(idx + 1, s + ar[idx])
 
for t in range(int(input())):
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    ans = 0
    F(0, 0)
    print("#{} {}".format(t+1, ans))