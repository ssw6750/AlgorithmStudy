n = int(input())
arr=[]
arr2=[]
stack=[]
ans=[]
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    arr2.append(i+1)

while(True):
    if len(stack)<=0 and len(arr2)>0:
        stack.append(arr2.pop(0))
        ans.append("+")
    else:
        if stack[-1] == arr[0]:
            stack.pop(-1)
            arr.pop(0)
            ans.append("-")
        else: 
            stack.append(arr2.pop(0))
            ans.append("+")
    if len(arr2)<=0:
        if len(stack)<=0:
            break
        else:
            if stack[-1] != arr[0]:
                break

if len(stack)>0:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])
