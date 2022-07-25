n = int(input())
arr=[]
flag=True
for i in range(n):
    arr.append(i+1)


while(True):
    if len(arr)==1:
        break
    if len(arr) % 2 == 0:
        tmp = True
    else: tmp = False
    if flag == False:
        arr.append(arr.pop(0))
    arr=arr[1::2]
    flag = tmp
print(arr[0])